from selenium import webdriver
from selenium.webdriver.common.by import By
from IPython.display import Image
from IPython.display import HTML
import pandas as pd
import time

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


print(input_name('Каламбет Владислав Борисович'))