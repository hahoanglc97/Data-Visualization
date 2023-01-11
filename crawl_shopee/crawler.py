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
shopee = crawl_util.load_links(crawl_util.SHOPEE_URL + 'search?keyword=', keywords)
shopee_mall = crawl_util.load_links(crawl_util.SHOPEE_URL + 'mall/search?keyword=', keywords)
links = shopee + shopee_mall
print(f'Total of {len(links)} links found.')

crawl_util.run_woker(links)
