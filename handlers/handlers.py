from aiogram import Router, F
from aiogram.client import bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

import payment
from states.states import UserStates
import command.keyboard as kb
import db.requests as db


router = Router()

@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    db.get_tg_id(message.from_user.id, message.from_user.username)
    await message.answer_photo(reply_markup=kb.choose_button(), caption="Добро пожаловать в магазин Канала SSB 🌎", photo="https://postimg.cc/mz4f3Vnr")
    await state.set_state(UserStates.user_choose_menu)

@router.callback_query(F.data == "profile", UserStates.user_choose_menu)
async def profile(callback: CallbackQuery, state: FSMContext):
    id = callback.from_user.id
    username = callback.from_user.username
    money = db.get_money(id)
    tuple = db.get_data(id)

    year = tuple[0].year
    month = tuple[0].month
    day = tuple[0].day

    await callback.message.edit_text(
        f"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n👤 Username: {username}\n🔑 id: {id}\n\n💳 Баланс: {','.join(money)} руб\n\n⏱ Дата регистрации: {year}:{db.get_full_data(day, month)}\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    await callback.message.edit_reply_markup(reply_markup=kb.profile())
    await state.set_state(UserStates.user_choose_profile)

@router.callback_query(F.data == "back", UserStates.user_choose_profile)
async def back_on_catalog(callback: CallbackQuery, state: FSMContext):

    await callback.message.edit_text(
        f"Меню SSB Store 📖")

    await callback.message.edit_reply_markup(reply_markup=kb.choose_button())
    await state.set_state(UserStates.user_choose_menu)

@router.callback_query(F.data == "info")
async def info(callback: CallbackQuery):

    await callback.answer()
    await callback.message.answer("Информация обо мне")

@router.callback_query(F.data == "product", UserStates.user_choose_menu)
async def product(callback: CallbackQuery, state: FSMContext):

    await callback.message.edit_text(
        f"Каталог товаров 📦", )

    await callback.message.edit_reply_markup(reply_markup=kb.catalog())
    await state.set_state(UserStates.user_choose_product)

@router.callback_query(F.data == "back", UserStates.user_choose_product)
async def back_on_catalog(callback: CallbackQuery, state: FSMContext):

    await callback.message.edit_text(
        f"Меню SSB Store 📖")

    await callback.message.edit_reply_markup(reply_markup=kb.choose_button())
    await state.set_state(UserStates.user_choose_menu)

@router.callback_query(F.data == "balance", UserStates.user_choose_profile)
async def balance(callback: CallbackQuery, state: FSMContext):

    url, payment_id = payment.create()

    await callback.message.edit_text(
        f"Оплата")

    await callback.message.edit_reply_markup(reply_markup=kb.buy(url, payment_id))

    await state.set_state(UserStates.user_pay)

@router.callback_query(UserStates.user_pay)
async def check_pay(callback: CallbackQuery, state: FSMContext):

    if callback.message['text'] == 'Оплата':

        otvet = payment.oplata_check(callback.data)
        if otvet:
            await callback.message.answer(chat_id=callback.from_user.id, text="Платёж прошёл успешно")
        else:
            await callback.message.answer(chat_id=callback.from_user.id, text="Платёж прошёл не успешно")

