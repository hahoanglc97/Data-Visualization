import requests

url = 'https://shopee.tw/api/v2/search_items/?by=pop&limit=30&match_id=1819984&newest=0&order=desc&page_type=shop&shop_categoryids=9271157&version=2'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://shopee.tw/shop/1819984/search?shopCollection=9271157',
}    

r = requests.get(url, headers=headers)

data = r.json()