from aiogram.dispatcher.filters.state import State, StatesGroup
class Information(StatesGroup): 
    name = State()
    info = State()
    word = State()

class InformationEdit(StatesGroup):
    editname = State()
    editinfo = State()