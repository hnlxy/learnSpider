import requests
from bs4 import BeautifulSoup

response = requests.get(
    url='https://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    }
)
soup = BeautifulSoup(response.text, features='html.parser')
# print(soup.prettify())
ul = soup.find(name='ul', attrs={'class': 'm-cvrlst f-cb', 'id': 'm-pl-container'})
# print(ul.prettify())

for li in ul.find_all(name='li', recursive=False):
    a = li.find(name='a', attrs={'class': 'msk'})
    img = li.find(name='img', attrs={'class': 'j-flag'})
    print(a.attrs['title'], img.attrs['src'])

    file_name = a.attrs['title'].split(' ')[-1]
    with open(f'./imgs/{file_name}.jpg', 'wb') as file:
        res = requests.get(img.attrs['src'])
        assert res.status_code == 200
        file.write(res.content)
