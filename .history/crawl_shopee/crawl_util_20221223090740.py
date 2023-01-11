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


SHOPEE_URL = 'https://shopee.vn/'
COUNT_NAME = 0

# create object for chrome 
def create_object_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome('./chromedriver', options = chrome_options)
    browser.implicitly_wait(5)
    return browser


# Link Extraction
def load_links(base_url, keywords):
    browser = create_object_chrome()
    links = []
    for keyword in keywords:
      try:
        browser.get(base_url + keyword)
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
    return links

# Extract Data From URL
def get_driver(create_new = False):
    threadLocal = threading.local()
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
def fetch_data_to_csv(url):
    name, price, favourite, rating = [], [], []
    noOfSold, brand, stock = [], [], []
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
        brand_value = 'None'
        stock_value = 'None'

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
        df = pd.DataFrame({
            'Product Name': name,
            'Price': price,
            'Favourite': favourite,
            'Brand':  brand,
            'Product Sold': noOfSold,
            'Stock': stock,
            'Rating': rating
        })
        df.to_csv('/data/data_raw.csv', sep='\t', encoding='utf-8')
        COUNT_NAME = len(name)
    except TimeoutException:
        print('TIMEOUT')
        driver = get_driver(True)
        sleep(3)
    except Exception as exc:
        print(f'[EXCEPTION]: {url} generated an exception: {exc}')

def run_woker(links):
    start_time = time.time()
    link_count = len(links)
    fetch_data_to_csv(links)
    # with concurrent.futures.ThreadPoolExecutor(max_workers = 20) as executor:
    #     executor.map(fetch_data_to_csv, links)
    #     executor.shutdown(wait=False)
    
    # Print Execution Result
    print(f"Elapsed run time: {time.time() - start_time} seconds.")
    print(f"Fetched {COUNT_NAME} out of {link_count} links.")
    print(f"Failed to fetch {link_count - COUNT_NAME} links due to exception/timeout.")