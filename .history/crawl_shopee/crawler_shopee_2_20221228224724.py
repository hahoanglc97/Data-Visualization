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

SHOPEE_URL = 'https://shopee.vn/'

keywords = [
            'Quan ao nu',
]

maxpages = 1

name, price, favourite = [], [], []
processor, weight = [], []
rating, model = [], []
noOfSold, brand, stock = [], [], []
links = []


# Initialize Selenium - create object for chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
ser = Service("./chromedriver")
browser = webdriver.Chrome(service=ser, options = chrome_options)
browser.implicitly_wait(5)
threadLocal = threading.local()

#------initial function----------
def load_links(base_url):
  for keyword in keywords:
    for page in range(0,maxpages):
        try:
            browser.get(base_url + keyword + ( ('&page='+ str(page)) if page > 0 else '') )
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.shopee-search-item-result__items'))) # Wait until `shop result` loaded within 10 secs or timeout

            # change second parameter in range function in scale of 1 - 5.
            # 1 = 20% (~15 links)
            # 2 = 40% (~25 links)
            # 3 = 60% (~40 links)
            # 4 = 80% (~55 links)
            # 5 = 100% (~60 links)
            for i in range(1, 1):
              browser.execute_script(f"window.scrollTo(document.body.scrollWidth * 0.3, document.body.scrollHeight * {i/5});")
              # WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._3GAFiR')))
              WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.shopee-search-item-result__items'))) # Wait until `shop result` loaded within 10 secs or timeout

            soup = BeautifulSoup(browser.page_source, "html.parser")
            key_links = soup.find_all(href=True, attrs={'data-sqe': 'link'})
            for a in key_links:
              links.append(a['href'].encode("ascii", "ignore").decode())

            print(f'Found {len(key_links)} link(s) in {keyword}')
        except TimeoutException:
            print("Timeout")
        except Exception as e:
            print(f"ERROR: {e}")

# Get product's links
load_links(SHOPEE_URL + 'search?keyword=')
# load_links(SHOPEE_URL + 'mall/search?keyword=')
print(f'Total of {len(links)} links found.')
pd.DataFrame(links, columns=['link']).to_csv("./crawl_shopee/data/links_product.csv")

