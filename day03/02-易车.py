import requests
from bs4 import BeautifulSoup

response = requests.get('https://car.yiche.com/')
# print(response.text)
soup = BeautifulSoup(markup=response.text, features='html.parser')
# print(soup.prettify()
div_list = soup.find_all(name='div', attrs={'class': 'item-brand'})
for div in div_list:
    # print(div.attrs['data-name'])
    child = div.find(name='div', attrs={'class': 'brand-name'})
    print(child.text)
