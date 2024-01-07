import requests
import json
from bs4 import BeautifulSoup

# response = requests.post(
#     url='https://passport.china.com/logon',
#     data='userName=15539482823&password=lxy000000&cookieTime=on',
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
#         'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
#         'Referer': 'https://passport.china.com/logon'
#     }
# )
# assert response.status_code == 200
# print(response.json()["msg"])
# print(response.cookies.get_dict())

cookies_dict = {'CHINACOMID': '1a1275e1-5764-4ddc-9d02-b3d3a04bad9b9', 'CP_USER': 'FKBo6w-aaDHf68gZInmcBZxFCjb%2FvF8dzIpsuaQNIsK3sMPBslaLzfBHzoZgt4tm51QsBDmimgCSkIT%2FOPV%2FPGumfJyC7TEPNAnY%2FL9Ms3FxJ3AiB%2FsQkvAm7Zn-AHLS-JSwT7Np%2FbXPkIoj7VkZppJmPIxyeXujIy1T3aPVirZd9eMaoKjnt6QOavL2l58jF6ZUs80x0PTUkQJnu8gY%2FIp8hft4-nM1kvviu%2FJ4kJsiC44IuLq2ow%3D%3D', 'CP_USERINFO': '4Gkk4uas%2FGU6V4cAn8Kr14YtZHaRsQ3bb0iKxhYvuaLYLT-rPEFbvbaQzjvqSKm2v8Fd1lQ14weg0PM1aAxGqjzFStaNWwdXEhS3Zzs0jusNqPIZSkWIUHBpa7NyrsBUv2O8QVvh3O4yqW9wAjnfpw%3D%3D', 'bindMobile': '"1@155*****823"', 'china_variable': 'jpEe7N32pYz8SAjCjL8fnh2eLZiI1D/EC6dYmS6/lLUOPrHJGj-IxLIHbACvhNcaC9z3Z8pi2hy0JtYoQGGXmsutg32di8lhAZaSKKJ8BFBt-lJZl7B3R-LY1hWhKpza', 'lastlogindate': '2024-01-03', 'lastloginip': '121.18.90.146', 'lastlogintime': '"11:01:39"', 'nickname': 'china_2885uluw16790299', 'SESSION_COOKIE': '118'}
response = requests.get(
    url='https://passport.china.com/main',
    cookies=cookies_dict
)
assert response.status_code == 200
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
div = soup.find(name='div', attrs={'class': 'm-logon-text'})
usernick = div.find('p', attrs={'class': 'm-l-t-user', 'id': 'usernick'}).text
logindate, loginIP = div.find('div', attrs={'class': 'm-l-t-info'}).find('p').strings
print(usernick, logindate, loginIP)
