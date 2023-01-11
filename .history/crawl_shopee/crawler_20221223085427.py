import os
from selenium import webdriver
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
import crawl_util

browser = crawl_util.create_object_chrome()
#Remove Language Option Overlay
browser.get(crawl_util.SHOPEE_URL)

popup = browser.find_elements(By.CLASS_NAME, 'home-popup')
for e in popup:
  if e.get_attribute('class') == 'shopee-popup__close-btn':
    e.click()
    break

# elements = browser.find_elements(By.CLASS_NAME, 'shopee-button-outline--primary-reverse')

# for e in elements:
#   if e.text == 'VietNam':
#     e.click()
#     break

##-----
keywords = [
            'MSI Laptop',
            'Dell Laptop',
            'Asus Laptop',
            'LG Laptop'
]
links = []
links.append(crawl_util.load_links(crawl_util.SHOPEE_URL + 'search?keyword='))
links.append(crawl_util.load_links(crawl_util.SHOPEE_URL + 'mall/search?keyword='))
print(f'Total of {len(links)} links found.')

start_time = time.time()
link_count = len(links)

with concurrent.futures.ThreadPoolExecutor(max_workers = 20) as executor:
  executor.map(crawl_util.fetch_data_to_csv, links)
  executor.shutdown(wait=False)

# Print Execution Result
print(f"Elapsed run time: {time.time() - start_time} seconds.")
# print(f"Fetched {len(name)} out of {link_count} links.")
# print(f"Failed to fetch {link_count - len(name)} links due to exception/timeout.")