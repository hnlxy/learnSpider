import requests
import json

response = requests.get(
    url='https://ke.qq.com/cgi-proxy/home/web_home_course?category1st=1000&model_id=3&must_not_courses=%5B%5D&page_num=4&page_size=19&platform=3&bkn=&r=0.2066',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
        'Referer': 'https://ke.qq.com/'
    },
    data={
        'category1st': 1000,
        'model_id': 3,
        'must_not_courses': [],
        'page_num': 4,
        'page_size': 19,
        'platform': 3,
        'r': 0.2066
    }
)
assert response.status_code == 200
# print(response.text)
data_dict = json.loads(response.text)
for index, web_course_item in enumerate(data_dict['result']['web_course_items']):
    print(index, web_course_item['web_home_courses']['agency_name'], web_course_item['web_home_courses']['course_name'])
