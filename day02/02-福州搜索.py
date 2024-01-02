import requests
import json

response = requests.post(
    url='https://www.fuzhou.gov.cn/ssp/search/api/search?time=1704170002976',
    data='siteType=1&mainSiteId=402849946077df37016077eea95e002f&siteId=402849946077df37016077eea95e002f&type=0&page=1&rows=10&historyId=48908a988c82508a018cc8729c83704f&sourceType=SSP_ZHSS&isChange=0&fullKey=N&wbServiceType=13&fileType=&fileNo=&pubOrg=&themeType=&searchTime=&startDate=&endDate=&sortFiled=RELEVANCE&searchFiled=&dirUseLevel=&issueYear=&issueMonth=&allKey=&fullWord=&oneKey=&notKey=&totalIssue=&chnlName=&zfgbTitle=&zfgbContent=&zfgbPubOrg=&zwgkPubDate=&zwgkDoctitle=&zwgkDoccontent=&zhPubOrg=1&keyWord=%E7%BC%96%E7%A8%8B&pubOrgType=&zhuTiIdList=&feaTypeName=&jiGuanList=&publishYear=',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
    }
)

# response = requests.post(
#     url='https://www.fuzhou.gov.cn/ssp/search/api/search?time=1704170002976',
#     data=json.dumps({}),
#     headers={
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
#         'Content-Type': 'application/json; charset=utf-8'
#     }
# )

assert response.status_code == 200
# print(response.text)
response_dict = json.loads(response.text)
for index, data in enumerate(response_dict['datas']):
    print(index, data['doctitle'], data['doccontent'])
