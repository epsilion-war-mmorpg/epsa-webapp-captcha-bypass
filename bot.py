import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from settings import app_settings

logger = logging.getLogger(__file__)
dp = Dispatcher()
bot = Bot(token=app_settings.bot_token)


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    answer = 'It is the web-app init handler'
    markup = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(
            text="Open webapp",
            web_app=WebAppInfo(url=app_settings.webapp_host),
        )]]
    )
    await message.answer(answer, reply_markup=markup)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
