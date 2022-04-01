from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
from bs4 import BeautifulSoup

url = 'http://gendalf.cf/'
response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, 'lxml')
name = soup.find('h1')
name1 = name.text
price_old = soup.find('h2')
price_old1 = price_old.text

TOKEN = "5232010643:AAE9OCbvEkKyKwvVoJWryHUxCkR_Q-yjug8"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Введите /lot для отслеживания товара")

@dp.message_handler(commands=['lot'])
async def process_start_command(message: types.Message):
    await message.answer(name1)
    price = soup.find('h2').text
    if price_old1 != price:
        await message.answer(price)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer("Введите название фильма и я отправлю рейтинг этого фильма по Кинопоиску и Imdb")

if __name__ == '__main__':
   executor.start_polling(dp)