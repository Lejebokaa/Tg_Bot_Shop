from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Профиль")],
   [KeyboardButton(text="Информация обо мне"), KeyboardButton(text="Баланс")],
   [KeyboardButton(text="Товар"), KeyboardButton(text="Отзывы")]
],
                            resize_keyboard=True,
                            input_field_placeholder="Выберите пункт меню.")
