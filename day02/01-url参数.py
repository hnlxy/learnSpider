import requests
import json

response = requests.get(
    url='https://movie.douban.com/j/search_subjects',
    params={
        'type': 'movie',
        'tag': '豆瓣高分',
        'page_limit': 50,
        'page_start': 0
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
    }
)
assert response.status_code == 200
# print(response.text)
response_dict = json.loads(response.text)
for index, subject in enumerate(response_dict['subjects']):
    print(index, subject["title"], subject["url"])
