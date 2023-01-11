from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
import threading
import pandas as pd
import concurrent.futures
import time

# create object for chrome 
def create_object_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome('./chromedriver', options = chrome_options)
    browser.implicitly_wait(5)
    threadLocal = threading.local()
    return browser, threadLocal