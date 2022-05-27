from telebot import types
from t_bot.states.base import BaseState


class Hello(BaseState):
    text = "Привет! Я помогу тебе найти квартиру в аренду на сайте OLX. Введи название города в Украине"

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data and message.data == 'nextstate:ActionState':
            return ActionState
        return Hello

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Акція', callback_data='nextstate:ActionState'))
        return keyboard


class ActionState(BaseState):
    text = "Вітаю, у нас діє акції! Оберіть: 1 - Новий рік, 2 - Багато хвилин, 3 - Скоро повернемо"

    def process_text_message(self, message: types.Message) -> 'BaseState':
        if message.text in ('1', '2', '3'):
            return ActionAppliedState
        self.send_warning('Натисніть 1, 2 або 3!')
        return ActionState


class ActionAppliedState(BaseState):
    text = "Вибачте, всі оператори зайняті!"

    def get_keyboard(self):
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='Додому', callback_data='nextstate:Hello'))
        return keyboard

    def process_call_back(self, message: types.CallbackQuery) -> 'BaseState':
        if message.data and message.data == 'nextstate:Hello':
            return Hello
        return ActionAppliedState