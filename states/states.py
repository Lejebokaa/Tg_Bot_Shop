from aiogram.fsm.state import State, StatesGroup

class UserStates(StatesGroup):
    user_start = State()
    user_choose_menu = State()
    user_choose_profile = State()
    user_choose_catalog = State()
    user_choose_product = State()
    user_pay = State()
    user_check_pay = State()
