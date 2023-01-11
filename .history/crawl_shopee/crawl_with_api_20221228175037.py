import requests

base_url = 'https://shopee.vn/api/v4/search/search_items? \
        by=relevancy&keyword={}& \
        limit=60& \
        newest={}& \
        order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2& \
        view_session_id=098aa3e6-8c83-44dd-9012-470b7f0c7c61'
url = base_url.format('quan%20ao%20nu', 0)
headers = {
    'af-ac-enc-dat': 'AAcyLjUuMC0yAAABhVhIDMgAAAi5AcAAAAAAAAAAAuvlR3weVVU60ykHUkkzSmQs+0sol/82EyfDx/bVRcPaaRvYm6Jw795TenP2FIMxWGojd+5CYTHXjTx2uZ0q5IEFrCDqU/NRgYYnzsuzJ01eBrIs55f7Ii6ulIGCuoQClFlVhPyX/zYTJ8PH9tVFw9ppG9ibIGsU32io2c0t1L/OeG3T0PVpNsS9ARiUdpQD6XANs1fnEduVg7AQsBYSODwqTI/lsp4AT4wxCM78yal8udwbJ3XZCXj/tkV27Cli4BSL6mZGrbfJWuRYlFp+J0tcUk6vzRxp09yVQMrFVCinn5W0MgNk3vgnob+rPTzbzZrb0eojVPTH9yx6ZZfQ2Upv2WNBdbuqwG8R8oiNo5jQim1n/RGyj4UWsmp6ms4Crd2heOyDz3lcCUAMGHhKIoDABfSoCsJdMewjePMrCAps8ZZxYlTqVgQr4Vdbt4WZVQflkkj3yNn/3TW2ljCJhOMYX/bEItVkNcbWy7Lk8j8rTPeYqZEul/dVd8VNHZ8sXHaEw3AJbQikjLNwW3HQ8tSNePyUzpHiv0VUkEKFJ2Z8iqzQSSQADndtlelH4VzH+caf8GOHwJz85YiD2Bc+r+V9F08q',
    'cookie': '__LOCALE__null=VN; csrftoken=kU4nPvtLnBSLZPZdF1u52S1ka40z0Jq6; SPC_F=rCBWqoshSo2UDCuuoAvcI44swwVoc1B2; REC_T_ID=65c0b09e-822f-11ed-aca2-2cea7fafb571; SPC_R_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_R_T_IV=UjlSU1RoY2NlZHVHaGRSMA==; SPC_T_ID=pmO6NuNVSS9KGNKnTbcZSTjZRmNXHIuY0PfowGtzZQeR1w3gFpo4kLZ3G/tjxtq32jEFq2HpWRVJVb2mWcdTFtbjc68WDuZ01JQmBeNxL7yViWPRPZuWQXSgm+WlV7UgVg0EizrYgta7dgrarmgPr0A8wlY4Xi6xosmQlZXiyXU=; SPC_T_IV=UjlSU1RoY2NlZHVHaGRSMA==; _QPWSDCXHZQA=0248ea48-b92f-4015-b4e1-6b7c46910ba5; SPC_SI=+++rYwAAAABUczVzekZVbILTAAAAAAAATTFqRlEzUkY=; SPC_SC_SA_TK=; SPC_SC_SA_UD=; shopee_webUnique_ccd=St3hNDUkpmNLatDMwiVNpw%3D%3D%7C5i%2BY5Gxz%2BR3QwzkdvzIFXZGWiBYCPUKNBfizSpB4yFPSeyX3Pzz6aQ7UyzgAGHD%2Br4sKR5OYh7JCpkWd6S5CkYC%2BybM%2Bk%2BdYnhc%3D%7CEbh6O9%2FEMsfP91lo%7C06%7C3; ds=429c9185a5825cd89aae34cfb4486a96'
}    

payload={}
response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()
for item in data:
    print('---')
