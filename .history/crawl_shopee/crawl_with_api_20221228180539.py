import requests
import json

url = "https://shopee.vn/api/v4/search/search_items?by=relevancy&keyword=quan%20ao%20nu&limit=60&newest=600&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=96c84449-ba7b-49dd-aced-e5b99ed42d5c"

payload={}
headers = {
  'af-ac-enc-dat': 'AAcyLjUuMC0yAAABhVhiAgQAAAipAcAAAAAAAAAAAuvlR3weVVU60ykHUkkzSmQs+0sol/82EyfDx/bVRcPaaRvYm6Jw795TenP2FIMxWGojd+5CYTHXjTx2uZ0q5IEFrCDqhXsd8CVdn3VWTzrGKzk5Dpf7Ii6ulIGCuoQClFlVhPyX/zYTJ8PH9tVFw9ppG9ibIGsU32io2c0t1L/OeG3T0PVpNsS9ARiUdpQD6XANs1fnEduVg7AQsBYSODwqTI/lsp4AT4wxCM78yal8udwbJ3XZCXj/tkV27Cli4BSL6mZGrbfJWuRYlFp+J0tcUk6vzRxp09yVQMrFVCinn5W0MgNk3vgnob+rPTzbzZrb0eojVPTH9yx6ZZfQ2Upv2WNBdbuqwG8R8oiNo5jQim1n/RGyj4UWsmp6ms4Crd2heOyDz3lcCUAMGHhKIoDABfSoCsJdMewjePMrCAps8ZZxYlTqVgQr4Vdbt4WZVQflkkj3yNn/3TW2ljCJhOMYX/bEItVkNcbWy7Lk8j8rTPeYqZEul/dVd8VNHZ8sXHaEw3AJbQikjLNwW3HQ8tSNePyUzpHiv0VUkEKFJ2Z8iqzQSSQADndtlelH4VzH+caf8GOHwJz85YiD2Bc+r+V9F08q',
  'content-type': 'application/json',
  'cookie': '__LOCALE__null=VN; csrftoken=kU4nPvtLnBSLZPZdF1u52S1ka40z0Jq6; SPC_F=rCBWqoshSo2UDCuuoAvcI44swwVoc1B2; REC_T_ID=65c0b09e-822f-11ed-aca2-2cea7fafb571; SPC_R_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_R_T_IV=UjlSU1RoY2NlZHVHaGRSMA==; SPC_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_T_IV=UjlSU1RoY2NlZHVHaGRSMA==; _QPWSDCXHZQA=0248ea48-b92f-4015-b4e1-6b7c46910ba5; SPC_SI=+++rYwAAAABUczVzekZVbILTAAAAAAAATTFqRlEzUkY=; SPC_SC_SA_TK=; SPC_SC_SA_UD=; shopee_webUnique_ccd=RdkuVf20mxcAYlSISIV13A%3D%3D%7C5yWY5Gxz%2BR3QwzkdvzIFXZGWiBYCPUKNBfizSpB4yFPSeyX3Pzz6aQ7UyzgAGHD%2Br4sKR5OYh7JCpkWd6S5FloG6xbU9k%2BdYnhc%3D%7CEbh6O9%2FEMsfP91lo%7C06%7C3; ds=fa66bae1f60f15612feda85e1ea92f28; REC_T_ID=88bfb76d-8687-11ed-b01f-10c17297d83b; SPC_F=T8ssmWcjk2G2UxJ6pw3SGiex03VW0Mvl; SPC_R_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_R_T_IV=UjlSU1RoY2NlZHVHaGRSMA==; SPC_SI=+++rYwAAAABUczVzekZVbILTAAAAAAAATTFqRlEzUkY=; SPC_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_T_IV=UjlSU1RoY2NlZHVHaGRSMA==',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"
}

response = requests.get(url, headers=headers)

print(response.text)
