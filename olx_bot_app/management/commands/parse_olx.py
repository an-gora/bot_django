import time
import traceback
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from django.core.management.base import BaseCommand
from olx_bot_app.models import Ad

BASE_URL = 'http://olx.ua'
AllAds = namedtuple('Ad', 'name,link,price,merts,city,')



class WaitSuggestion:
    def __init__(self, txt=''):
        self.__text = txt

    def __call__(self, driver: webdriver.Chrome, *args, **kwargs):
        suggestions = [e for e in driver.find_elements_by_tag_name("li") if
                       e.get_attribute("data-testid") == "suggestion-item"]
        if len(suggestions) > 0:
            if suggestions[0].text == "":
                return False
            return True
        return False


class WaitTextChange:
    def __init__(self, div):
        self.__div_text = div.text
        self.__div = div

    def __call__(self, *args, **kwargs):
        return self.__div_text != self.__div.text



class SingleAd(AllAds):

    def __str__(self):
        return (f'{self.name}, {self.link}, {self.price}, {self.city}, {self.metr}')


class Olx_parser:

    def __init__(self):
        self.all_ads = []

    def parse_olx(self):
        # d = webdriver.Chrome('./chromedriver')
        d = webdriver.Chrome('/home/nastya/PycharmProjects/chromedriver_linux64/chromedriver')
        # d = webdriver.Chrome()
        d.get(BASE_URL)
        # d.maximize_window()
        el = d.find_element_by_xpath('/html/body/div[1]/div[11]/button')
        el.click()
        WebDriverWait(d, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'maincategories'))
        )
        div1 = d.find_elements_by_class_name('maincategories')[0]
        link = div1.find_elements_by_tag_name('a')[2]
        link.click()
        WebDriverWait(d, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'a'))
        )
        for link in d.find_elements_by_tag_name('a'):
            if link.text == '????????????????':
                break
        else:
            print("something went wrong")
            exit(0)
        link.click()

        WebDriverWait(d, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'input'))
        )
        time.sleep(2)
        location = d.find_elements_by_tag_name('input')[1]
        location.send_keys('??????????????')
        WebDriverWait(d, 30).until(
            WaitSuggestion('??????????????')
        )

        suggestions = [e for e in d.find_elements_by_tag_name("li") if
                       e.get_attribute("data-testid") == "suggestion-item"]
        suggestions[0].click()

        chose = d.find_elements_by_class_name('css-12snx2d')
        chose[0].click()
        flat_for_rent = d.find_elements_by_class_name('css-1oi36r6')
        flat_for_rent[2].click()

        div_search_result = d.find_element_by_class_name('listing-grid-container')
        WebDriverWait(d, 20).until(
            WaitTextChange(div_search_result)
        )
        time.sleep(2)
        # d.find_element_by_name("searchBtn")
        print("find rezults")
        return div_search_result

    def save_results(self, div_search_result):
        search_divs = [
            e for e in div_search_result.find_elements_by_tag_name('div')
            if e.get_attribute("data-cy") == "l-card"
        ]
        print(len(search_divs))
        rez = []
        for div in search_divs:
            try:
                # current_ad = SingleAd
                SingleAd.name = div.find_element_by_tag_name('h6').text
                SingleAd.link = div.find_element_by_class_name('css-1bbgabe').get_attribute('href')
                SingleAd.price, SingleAd.city, SingleAd.metr = [e.text for e in div.find_elements_by_tag_name('p')]
                SingleAd.city = SingleAd.city.rpartition(' - ')[0]
            except:
                print(traceback.format_exc())
                pass

            try:
                ad = Ad.objects.get(url=SingleAd.link)
                ad.title=SingleAd.name,
                ad.price=SingleAd.price,
                ad.city = SingleAd.city,
                ad.metrs = SingleAd.metr,
                ad.save()
            except Ad.DoesNotExist:
                ad = Ad(
                    title=SingleAd.name,
                    url=SingleAd.link,
                    price=SingleAd.price,
                    city=SingleAd.city,
                    metrs=SingleAd.metr,
                ).save()
        # return re

    def collect_all(self):
        div_search_result = self.parse_olx()
        self.save_results(div_search_result)


class Command(BaseCommand):
    help = 'olx parsing'

    def handle(self, *args, **options):
        p = Olx_parser()
        p.collect_all()
