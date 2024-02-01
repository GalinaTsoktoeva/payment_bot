import os
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import router

load_dotenv('.env')
my_token = os.getenv("TELEGRAM_TAKEN")

async def main():
    print(my_token)
    bot = Bot(token=my_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
