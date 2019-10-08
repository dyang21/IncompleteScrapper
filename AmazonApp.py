# Allows me to get data from URL; BS4 is for parsing and pulling specific data

import requests
from bs4 import BeautifulSoup


URL = "https://www.target.com/p/old-spice-swagger-2-in-1-shampoo-and-conditioner-25-3-fl-oz/"
# Allows me to get information from my browser

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
                 }


page = requests.get(URL, headers=headers)
print(page.status_code)


soup1 = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')


# Pull information out using f12
title = soup2.find(id= "productTitle")

print(title)

# mission failed. make the html code in javascript.