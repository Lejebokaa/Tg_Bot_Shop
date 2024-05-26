from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def choose_button():

    choose_button = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text="Профиль 👤", callback_data="profile")],
       [InlineKeyboardButton(text="Информация обо мне 👑", callback_data="info"), InlineKeyboardButton(text="Тех поддержка ⚙️", url="https://t.me/ssbwqa")],
       [InlineKeyboardButton(text="Товар 📦", callback_data="product"), InlineKeyboardButton(text="Отзывы 📝", url="https://t.me/ssbmersh")]
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")
    return choose_button

def profile():

    profile = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text="Пополнить баланс 💳", callback_data="balance")],
       [InlineKeyboardButton(text="Меню 📖", callback_data="back")]
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")
    return profile

def catalog():
    catalog = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Футболки 👕", callback_data="t-shirts"), InlineKeyboardButton(text="Худи 🧥", callback_data="hoodies")],
        [InlineKeyboardButton(text="Шорты 🩳", callback_data="shorts"), InlineKeyboardButton(text="Штаны 👖", callback_data="pants")],
        [InlineKeyboardButton(text="Меню 📖", callback_data="back")]
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")
    return catalog

def buy(url, id):
    pay = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Ссылка", url=url)],
        [InlineKeyboardButton(text="Проверить оплату", callback_data=id)]
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")
