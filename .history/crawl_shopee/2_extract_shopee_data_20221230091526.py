import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
from collections import Counter
import threading
import time
import pandas as pd
import numpy as np
from numpy import nan
import re
import concurrent.futures
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Initialize Selenium - create object for chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
ser = Service("./chromedriver")
browser = webdriver.Chrome(service=ser, options = chrome_options)
browser.implicitly_wait(5)
threadLocal = threading.local()


def get_driver(create_new = False):
  driver = getattr(threadLocal, 'driver', None)

  if driver is None or create_new:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    ser = Service("./chromedriver")
    driver = webdriver.Chrome(service=ser, options = chrome_options)
    # driver = webdriver.Chrome('./chromedriver', options = chrome_options)
    setattr(threadLocal, 'driver', driver)
    
  return driver

# Fetching Data
def fetch_data(url):
    try:
      print(f'[{threading.current_thread().name}] Fetching data from {url}...')

      driver = get_driver()
      driver.get(SHOPEE_URL + url[1:])
      WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.X0xUb5'))) # Wait until `price` loaded within 10 secs or timeout

      soup = BeautifulSoup(driver.page_source, "html.parser")

      ## ONLY Change below
      price_value = getattr(soup.select_one('.X0xUb5'), 'text', 'None')
      name_value = getattr(soup.select_one('.YPqix5 > span'), 'text', 'None')
      rating_value = getattr(soup.select('.gS2iLG > .yz-vZm')[0], 'text', 'None')
      favourite_value = getattr(soup.select('.gS2iLG > .yz-vZm')[1], 'text', 'None')
      sold_value = getattr(soup.select_one('div.yiMptB'), 'text', 'None')
      cpu_value = 'None'
      weight_value = 'None'
      brand_value = 'None'
      stock_value = 'None'
      model_value = 'None'

      specs = soup.select('.VYmrqq')
      for col in specs:
        key = col.select_one('label.zgeHL-').text
        value = getattr(col.select_one('div'), 'text', 'None')

        if 'Brand' in key and col.select_one('a') != None:
          brand_value = col.select_one('a').text
        
        if 'Thương hiệu' in key and col.select_one('a') != None:
          brand_value = col.select_one('a').text

        if 'Stock' in key and value != 'None':
          stock_value = value

        if 'Kho hàng' in key and value != 'None':
          stock_value = value

      price.append(price_value)
      name.append(name_value)
      favourite.append(favourite_value)
      brand.append(brand_value)
      noOfSold.append(sold_value)
      stock.append(stock_value)
      rating.append(rating_value)

    except TimeoutException:
      print('TIMEOUT')
      driver = get_driver(True)
      sleep(3)
    except Exception as exc:
      print(f'[EXCEPTION]: {url} generated an exception: {exc}')