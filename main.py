from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "5774623601:AAE7Mjcq5frB1nhWAWfw6xN5QODteAyWyF4"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot) #диспетчер, анализирует все входящие запросы

@dp.message_handler()                             # отвечает на все сообщения
async def echo(message: types.Message):
    await message.answer(text=message.text.upper)

if __name__ == '__main__':
    executor.start_polling(dp)