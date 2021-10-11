import requests
from bs4 import BeautifulSoup

URL = 'https://mainstreetbooks.co.uk/shop-fiction/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find(class_='products')
books = content.find_all('li')

for book in books:
    title_elem = book.find('h2', class_='woocommerce-loop-product__title')
    price_elem = book.find('span', class_='price')
    if None in title_elem:
        continue
    title = title_elem.text.strip()
    title = title.split('by')
    if len(title) > 1 and title[1].lower().strip() == 'philip pullman':
        print(title[0].strip())
        print('By ' + title[1].strip())
        print(price_elem.text.strip())
        print()
