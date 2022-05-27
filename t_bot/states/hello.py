from telebot import types

from olx_bot_app.models import Subscriber, Ad
from t_bot.states.base import BaseState


class Hello(BaseState):
    text = "Привет! Я помогу тебе найти квартиру в аренду на сайте OLX. Введи название города в Украине"

    def save_subscribe(self):
        # subscriber = Subscriber.objects.get_or_create(chat_id=self.chat_id)
        # last_apartment = Ad.objects.latest('id').url
        # self.bot.send_message(self.chat_id, last_apartment)
        self.bot.send_message(self.chat_id, 'test')


    def process_call_back(self, message: types.CallbackQuery):
        if message.data and message.data == 'nextstate:ActionState':
            self.save_subscribe()
            return ActionState
        return Hello

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Акція', callback_data='nextstate:ActionState'))
        return keyboard


class ActionState(BaseState):
    text = "выбрать 1 2 3 "

    def process_text_message(self, message: types.Message):
        if message.text in ('1', '2', '3'):
            return SubscribedState
        self.send_warning('Натисніть 1, 2 або 3!')
        return ActionState


# class ActionAppliedState(BaseState):
#     text = "Вибачте, всі оператори зайняті!"
#
#     def get_keyboard(self):
#         keyboard = types.InlineKeyboardMarkup()
#         keyboard.add(types.InlineKeyboardButton(text='Додому', callback_data='nextstate:Hello'))
#         return keyboard
#
#     def process_call_back(self, message: types.CallbackQuery):
#         if message.data and message.data == 'nextstate:Hello':
#             return Hello
#         return ActionAppliedState


class SubscribedState(BaseState):
    text = 'Вы успешно подписались на новые обьявления о сдаче квартир'

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(
            types.InlineKeyboardButton(text='Отменить подписку', callback_data='nextstate:Hello'))
        return keyboard

# from telebot import types
#
# from olx_bot_app.models import Ad, Subscriber
# from t_bot.states.base import BaseState
#
#
# class Hello(BaseState):
#     text = "Привет! Я помогу тебе найти квартиру в аренду в Украине. Введи название города"
#
#     def save_subscribe(self):
#         subscriber = Subscriber.objects.get_or_create(chat_id=self.chat_id)
#         last_apartment = Ad.objects.latest('id').url
#         self.bot.send_message(self.chat_id, last_apartment)
#
#         # last_news = News.objects.latest('date').link
#         # self.bot.send_message(self.chat_id, last_news)
#
#     def process_call_back(self, message: types.CallbackQuery):
#         if message.data and message.data == 'nextstate:SubscribedState':
#             self.save_subscribe()
#             return SubscribedState
#         return Hello
#
#     def get_keyboard(self):
#         keyboard = types.InlineKeyboardMarkup()
#         keyboard.add(
#             types.InlineKeyboardButton(text='Пiдписатися на всi новини', callback_data='nextstate:SubscribedState'))
#         return keyboard
#
#
# class SubscribedState(BaseState):
#     text = 'Вы успешно подписались на новые обьявления о сдаче квартир'
#
#     def get_keyboard(self):
#         keyboard = types.InlineKeyboardMarkup()
#         keyboard.add(
#             types.InlineKeyboardButton(text='Отменить подписку', callback_data='nextstate:Hello'))
#         return keyboard
