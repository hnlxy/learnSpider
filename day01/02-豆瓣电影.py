import requests
import json

response = requests.get(
    url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT'
    }
)
assert response.status_code == 200
# print(response.text)
response_dict = json.loads(response.text)
for index, subject in enumerate(response_dict['subjects']):
    print(index, subject["title"], subject["url"])
