from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('')
products=[] #List to store name of the product
prices=[] #List to store price of the product
driver.get('https://www.flipkart.com/search?q=Mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&as-pos=1&as-type=HISTORY&as-backfill=on')
content = driver.page_source
soup = BeautifulSoup(content,features="lxml")

for a in soup.findAll(attrs={'class':'yKfJKb row'}):
    name=a.find('div', attrs={'class':'KzDlHZ'})
    price=a.find('div', attrs={'class':'Nx9bqj _4b5DiR'})
    products.append(name.text)
    prices.append(price.text)

df = pd.DataFrame({'Product Name':products,'Price':prices})
df.to_csv('products.csv', index=False, encoding='utf-8')