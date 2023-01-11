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
import constants as const
import crawl_util as util
from tqdm import tqdm

browser, threadLocal = util.create_object_chrome()

name, price = [], []
rating, customer_rating = [], []
noOfSold, brand, stock, categories = [], [], [], []
five_start, four_start, three_start, two_start, one_start = [], [], [], [], []
comments, image_video_comments = [], []
links_timeout = []

def get_driver(create_new = False):
  global threadLocal
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
      # print(f'[{threading.current_th3read().name}] Fetching data from {url}...')
      print(f'Fetching data from {url}...')

      driver = get_driver()
      driver.get(const.SHOPEE_URL + url[1:])
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.X0xUb5'))) # Wait until `price` loaded within 10 secs or timeout
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight) * 0.5;")
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product-ratings'))) # Wait until `price` loaded within 10 secs or timeout

      soup = BeautifulSoup(driver.page_source, "html.parser")

      ## ONLY Change below
      price_value = getattr(soup.select_one('.X0xUb5'), 'text', 'None')
      name_value = getattr(soup.select_one('.YPqix5 > span'), 'text', 'None')
      rating_value = getattr(soup.select('.gS2iLG > .yz-vZm')[0], 'text', 'None')
      customer_rating_value = getattr(soup.select('.gS2iLG > .yz-vZm')[1], 'text', 'None')
      sold_value = getattr(soup.select_one('div.yiMptB'), 'text', 'None')
      brand_value = 'None'
      stock_value = 'None'
      categories_value = 'None'

      specs = soup.select('.VYmrqq')
      for col in specs:
        key = col.select_one('label.zgeHL-').text
        value = getattr(col.select_one('div'), 'text', 'None')

        if 'Danh Mục' in key and col.select_one('a') != None:
          categories_list = [value.text for value in col.select('a')[1:]]
          categories_value = '/'.join([str(elem) for elem in categories_list])
        
        if 'Thương hiệu' in key and col.select_one('a') != None:
          brand_value = col.select_one('a').text

        if 'Kho hàng' in key and value != 'None':
          stock_value = value


      rating_details = soup.select('.product-rating-overview__filter')
      five_start_value = rating_details[1].text
      four_start_value = rating_details[2].text
      three_start_value = rating_details[3].text
      two_start_value = rating_details[4].text
      one_start_value = rating_details[5].text
      comments_value = rating_details[6].text
      image_video_comments_value = rating_details[7].text

      price.append(price_value)
      name.append(name_value)
      brand.append(brand_value)
      categories.append(categories_value)
      noOfSold.append(sold_value)
      stock.append(stock_value)
      rating.append(rating_value)
      customer_rating.append(customer_rating_value)
      five_start.append(five_start_value)
      four_start.append(four_start_value)
      three_start.append(three_start_value)
      two_start.append(two_start_value)
      one_start.append(one_start_value)
      comments.append(comments_value)
      image_video_comments.append(image_video_comments_value)

    except TimeoutException:
      links_timeout.append(url)
      # print('TIMEOUT')
      driver = get_driver(True)
      sleep(3)
    except Exception as exc:
      print(f'[EXCEPTION]: {url} generated an exception: {exc}')

# os.makedirs(const.EXTRACTED_FOLDER, exist_ok=True)
# for file_path in os.listdir(const.DATASET_FOLDER):
#   if file_path not in const.CLASS_FILE:
#     continue
#   product_class = file_path.replace('links_product_','').replace('.csv','')

links = pd.read_csv(const.DATASET_FOLDER + const.CLASS_FILE[0])['link']
# links = pd.read_csv(f'{const.DATASET_FOLDER}test.csv')['link']
links.drop_duplicates(inplace=True)

# Extract Data From URL
threadLocal = threading.local()
start_time = time.time()
link_count = len(links)
# with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor:
#   executor.map(fetch_data, links)
#   executor.shutdown(wait=False)
for i in range(0,2):
  start = i * 10
  end = (i + 1) * 10 - 1
  if i == 18:
      end = -1
  mini_batch = links[start:end]
  # for url in tqdm(mini_batch):
  #   fetch_data(url)
  with concurrent.futures.ThreadPoolExecutor(max_workers = 10) as executor:
    executor.map(fetch_data, mini_batch)
    executor.shutdown(wait=False)
  df = pd.DataFrame({
    'Product Name': name,
    'Price': price,
    'Brand':  brand,
    'Categories': categories,
    'Product Sold': noOfSold,
    'Stock': stock,
    'Rating': rating,
    '5 Start': five_start,
    '4 Start': four_start,
    '3 Start': three_start,
    '2 Start': two_start,
    '1 Start': one_start,
    'Total Rating': customer_rating,
    'No of Comments': comments,
    'Image and Video': image_video_comments
  })
  df.to_csv(f'{const.EXTRACTED_FOLDER}thoi_trang/result_{i}.csv')
  name, price = [], []
  rating, customer_rating = [], []
  noOfSold, brand, stock, categories = [], [], [], []
  five_start, four_start, three_start, two_start, one_start = [], [], [], [], []
  comments, image_video_comments = [], []
# Print Execution Result
print(f"Elapsed run time: {time.time() - start_time} seconds.")
print(f"Fetched {len(name)} out of {link_count} links.")
print(f"Failed to fetch {link_count - len(name)} links due to exception/timeout.")



df_timeout = pd.DataFrame(links_timeout, columns=['link'])
df_timeout.to_csv(f'{const.EXTRACTED_FOLDER}timeout.csv')