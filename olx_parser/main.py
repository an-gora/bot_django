# import json
# import time
# import traceback
#
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# class WaitSuggestion:
#     def __init__(self, txt=''):
#         self.__text = txt
#
#     def __call__(self, driver: webdriver.Chrome, *args, **kwargs):
#         suggestions = [e for e in driver.find_elements_by_tag_name("li") if
#                        e.get_attribute("data-testid") == "suggestion-item"]
#         if len(suggestions) > 0:
#             if suggestions[0].text == "":
#                 return False
#             return True
#         return False
#
#
# class WaitTextChange:
#     def __init__(self, div):
#         self.__div_text = div.text
#         self.__div = div
#
#     def __call__(self, *args, **kwargs):
#         return self.__div_text != self.__div.text
#
#
# d = webdriver.Chrome('./chromedriver_linux64/chromedriver')
# d.get("http://olx.ua")
# # d.maximize_window()
# el = d.find_element_by_xpath('/html/body/div[1]/div[11]/button')
# el.click()
# WebDriverWait(d, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, 'maincategories'))
# )
# div1 = d.find_elements_by_class_name('maincategories')[0]
# link = div1.find_elements_by_tag_name('a')[2]
# link.click()
# WebDriverWait(d, 10).until(
#     EC.element_to_be_clickable((By.TAG_NAME, 'a'))
# )
# for link in d.find_elements_by_tag_name('a'):
#     if link.text == 'Квартиры':
#         break
# else:
#     print("AAAAAAAAAAAAAAAAAAAAa")
#     exit(0)
# link.click()
#
# WebDriverWait(d, 10).until(
#     EC.element_to_be_clickable((By.TAG_NAME, 'input'))
# )
# # WebDriverWait(driver, SEC_WAIT_ACTIVE).until(
# #             EC.element_to_be_clickable((By.CLASS_NAME, "js-lcc-accept"))
# #         ).click()
# time.sleep(2)
# location = d.find_elements_by_tag_name('input')[1]
# location.send_keys('Ужгород')
# WebDriverWait(d, 30).until(
#     WaitSuggestion('Ужгород')
# )
#
# suggestions = [e for e in d.find_elements_by_tag_name("li") if e.get_attribute("data-testid") == "suggestion-item"]
# suggestions[0].click()
#
# chose = d.find_elements_by_class_name('css-12snx2d')
# chose[0].click()
# flat_for_rent = d.find_elements_by_class_name('css-1oi36r6')
# flat_for_rent[2].click()
#
# div_search_result = d.find_element_by_class_name('listing-grid-container')
# WebDriverWait(d, 15).until(
#     WaitTextChange(div_search_result)
# )
# time.sleep(2)
# # d.find_element_by_name("searchBtn")
# print("find rezults")
# search_divs = [
#     e for e in div_search_result.find_elements_by_tag_name('div')
#     if e.get_attribute("data-cy") == "l-card"
# ]
# print(len(search_divs))
# rez = []
# for div in search_divs:
#     try:
#         name = div.find_element_by_tag_name('h6').text
#         link = div.find_element_by_class_name('css-1bbgabe').get_attribute('href')
#         price, address, metr = [e.text for e in div.find_elements_by_tag_name('p')]
#         rez.append({
#             # "name": name, "price": price, "addr": address, "metr": metr, "link":link
#             "name": name, "price": price, "addr": address, "metr": metr, "link": link
#         })
#     except:
#         print(traceback.format_exc())
#         pass
#
# with open("found.json", "w") as fp:
#     json.dump(rez, fp, indent=4, ensure_ascii=False)
#
# # d.close()