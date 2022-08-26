from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#1702048062:AAFtVDbQpLLz4rzInE11a6rID1ZMxGPeYf0
bot = Bot('5796227133:AAGjNB_wi6chVwa5HMLEGz48YXaEDIQHWLI', parse_mode='html')

#bot = Bot('2045002012:AAFVJUiqvABmN6wBRN3kN8jFMoXQtF07TbJ', parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())
#1001532093909, 1001723460895
chats = ['-1001558283749', '-1001599277773']


LOG_CHAT = '-507669812'

ADMINS = [944678884]