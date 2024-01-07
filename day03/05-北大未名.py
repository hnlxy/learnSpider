import hashlib

import requests
import time
import json
from bs4 import BeautifulSoup

username = 'zhangkai'
password = '123123'
ctime = int(time.time())
md5_str = password + username + str(ctime) + password
md5_obj = hashlib.md5(md5_str.encode('utf-8'))
print(md5_obj.hexdigest())

response = requests.post(
    url='https://bbs.pku.edu.cn/v2/ajax/login.php',
    data=f'username={username}&password={password}&keepalive=1&time={ctime}&t={md5_obj.hexdigest()}',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
)
print(response.text)
