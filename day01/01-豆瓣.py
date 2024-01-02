import requests
import json

res = requests.get(
    url="https://api.huaban.com/search/file?text=%E7%BE%8E%E5%A5%B3&sort=all&limit=40&page=1&position=search_pin&fields=pins:PIN,total,facets,split_words,relations,recommend_topics"
)
# print(res.headers)
data_dict = json.loads(res.text)
pin_list = data_dict["pins"]
for index, pin in enumerate(pin_list):
    print(index, pin["user"]["username"], pin["board"]["title"])
