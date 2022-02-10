from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import Image
from IPython.display import HTML
import pandas as pd
import time
import nest_asyncio
import logging
nest_asyncio.apply()
import aiogram
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36')
options.add_argument('window-size=1920,1080')
def input_name(name):
  wd = webdriver.Chrome(options=options)
  wd.get('https://zhituli.rosfirm.info/rostov%27')
  form = wd.find_elements_by_class_name('myform')[0]
  form.send_keys(name)
  click = wd.find_elements(By.NAME, 'searchButton')[0]
  click.click()
  time.sleep(2)
  f = wd.find_element(By.TAG_NAME, 'table')
  return f.text.split('\n')[1:]



TOKEN = '5253209009:AAEggr19tufH4iAXmE3zJruBqQbPLVaxpEw'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Введите ФИО")

@dp.message_handler()
async def process_name(message: types.Message):
  name = message.text
  await message.answer(''.join(input_name(name)))

if 'name' == 'main':
  executor.start_polling(dp)