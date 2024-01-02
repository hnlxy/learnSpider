import requests
from bs4 import BeautifulSoup

html_string = """<div>
    <h1 class="item">武沛奇</div>
    <ul class="item">
        <li>篮球</li>
        <li>足球</li>
    </ul>
    <div>
        <span>5xclass.cn</span>
        <a href="www.xxx.com" class="info">python.com</a>
    </div>
</div>"""

soup = BeautifulSoup(html_string, features='html.parser')
tag = soup.find(name='ul')
tag_l = tag.find_all(name='li')
# print(tag_l)
for li in tag_l:
    print(li.text)
