from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states.states import UserStates
import command.keyboard as kb
router = Router()

@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    await message.answer(
        text="Привет это бот канала SSB 👋 сдесь ты сможешь прикупить чёткий мерч 👕 от самого лучшего тг канала 👑 SSB Снизу появиться меню 📖 выберай что тебе нужно, удачи",
        reply_markup=kb.main)

    await state.set_state(UserStates.user_choose_menu)


