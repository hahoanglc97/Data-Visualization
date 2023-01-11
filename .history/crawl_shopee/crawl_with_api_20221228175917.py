import requests
import json

url = "https://shopee.vn/api/v4/search/search_items?by=relevancy&keyword=quan%20ao%20nu&limit=60&newest=600&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=96c84449-ba7b-49dd-aced-e5b99ed42d5c"

payload={}
headers = {
  'authority': 'shopee.vn',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
  'af-ac-enc-dat': 'AAcyLjUuMC0yAAABhVhiAgQAAAipAcAAAAAAAAAAAuvlR3weVVU60ykHUkkzSmQs+0sol/82EyfDx/bVRcPaaRvYm6Jw795TenP2FIMxWGojd+5CYTHXjTx2uZ0q5IEFrCDqhXsd8CVdn3VWTzrGKzk5Dpf7Ii6ulIGCuoQClFlVhPyX/zYTJ8PH9tVFw9ppG9ibIGsU32io2c0t1L/OeG3T0PVpNsS9ARiUdpQD6XANs1fnEduVg7AQsBYSODwqTI/lsp4AT4wxCM78yal8udwbJ3XZCXj/tkV27Cli4BSL6mZGrbfJWuRYlFp+J0tcUk6vzRxp09yVQMrFVCinn5W0MgNk3vgnob+rPTzbzZrb0eojVPTH9yx6ZZfQ2Upv2WNBdbuqwG8R8oiNo5jQim1n/RGyj4UWsmp6ms4Crd2heOyDz3lcCUAMGHhKIoDABfSoCsJdMewjePMrCAps8ZZxYlTqVgQr4Vdbt4WZVQflkkj3yNn/3TW2ljCJhOMYX/bEItVkNcbWy7Lk8j8rTPeYqZEul/dVd8VNHZ8sXHaEw3AJbQikjLNwW3HQ8tSNePyUzpHiv0VUkEKFJ2Z8iqzQSSQADndtlelH4VzH+caf8GOHwJz85YiD2Bc+r+V9F08q',
  'content-type': 'application/json',
  'cookie': '__LOCALE__null=VN; csrftoken=kU4nPvtLnBSLZPZdF1u52S1ka40z0Jq6; SPC_F=rCBWqoshSo2UDCuuoAvcI44swwVoc1B2; REC_T_ID=65c0b09e-822f-11ed-aca2-2cea7fafb571; SPC_R_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_R_T_IV=UjlSU1RoY2NlZHVHaGRSMA==; SPC_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_T_IV=UjlSU1RoY2NlZHVHaGRSMA==; _QPWSDCXHZQA=0248ea48-b92f-4015-b4e1-6b7c46910ba5; SPC_SI=+++rYwAAAABUczVzekZVbILTAAAAAAAATTFqRlEzUkY=; SPC_SC_SA_TK=; SPC_SC_SA_UD=; shopee_webUnique_ccd=RdkuVf20mxcAYlSISIV13A%3D%3D%7C5yWY5Gxz%2BR3QwzkdvzIFXZGWiBYCPUKNBfizSpB4yFPSeyX3Pzz6aQ7UyzgAGHD%2Br4sKR5OYh7JCpkWd6S5FloG6xbU9k%2BdYnhc%3D%7CEbh6O9%2FEMsfP91lo%7C06%7C3; ds=fa66bae1f60f15612feda85e1ea92f28; REC_T_ID=88bfb76d-8687-11ed-b01f-10c17297d83b; SPC_F=T8ssmWcjk2G2UxJ6pw3SGiex03VW0Mvl; SPC_R_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_R_T_IV=UjlSU1RoY2NlZHVHaGRSMA==; SPC_SI=+++rYwAAAABUczVzekZVbILTAAAAAAAATTFqRlEzUkY=; SPC_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_T_IV=UjlSU1RoY2NlZHVHaGRSMA==',
  'referer': 'https://shopee.vn/search?keyword=quan%20ao%20nu&page=10',
  'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sz-token': 'RdkuVf20mxcAYlSISIV13A==|5yWY5Gxz+R3QwzkdvzIFXZGWiBYCPUKNBfizSpB4yFPSeyX3Pzz6aQ7UyzgAGHD+r4sKR5OYh7JCpkWd6S5FloG6xbU9k+dYnhc=|Ebh6O9/EMsfP91lo|06|3',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
  'x-api-source': 'pc',
  'x-csrftoken': 'kU4nPvtLnBSLZPZdF1u52S1ka40z0Jq6',
  'x-requested-with': 'XMLHttpRequest',
  'x-sap-access-f': '3.2.108.6.0|13|2.5.0-2_5.1.0_0_170|f1661e7054294b4e92bac8a3798aeb334c2f3d9c086145|10900|1100',
  'x-sap-access-s': 'rlGP2DIm0cQd1lfIkDRKQX6JFoKqlKlfvA8vIRWmlWk=',
  'x-sap-access-t': '1672225096',
  'x-shopee-language': 'vi'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
