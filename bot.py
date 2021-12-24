from aiogram import executor
import aiogram
from dispatcher import dp
import handlers
from aiogram import Bot, Dispatcher, executor, types


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text[:5])
    print(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
