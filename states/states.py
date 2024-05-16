from aiogram.fsm.state import State, StatesGroup

class UserStates(StatesGroup):
    user_start = State()
    user_choose_menu = State()