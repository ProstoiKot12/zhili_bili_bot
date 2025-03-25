from aiogram.fsm.state import State, StatesGroup


class Enroll(StatesGroup):
    parent_name = State()
    child_name = State()
    child_age_old = State()
    parent_phone = State()
    