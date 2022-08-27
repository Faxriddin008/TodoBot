from aiogram import Bot, Dispatcher, executor, types
import  logging

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token= "", parse_mode='html')
dp = Dispatcher(bot=bot)

if __name__ =='__name__':
    executor.start_polling(dispather=dp)