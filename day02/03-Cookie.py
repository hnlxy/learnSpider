import requests
import json

response = requests.get(
    url='https://api.bilibili.com/x/member/web/account?web_location=333.33',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
        'cookie': 'innersign=0; buvid3=F8FE61FA-A201-177E-51D4-4E1C099C19EE40218infoc; b_nut=1704179540; i-wanna-go-back=-1; b_ut=7; b_lsid=226738F4_18CC9042246; bsource=search_bing; _uuid=7DA741D5-CB6D-10E7B-EBE10-D5CAECCA2BA140557infoc; buvid_fp=d3fc1267f658737c23015a82a81eb36f; buvid4=B128BE0E-C70E-2224-51C5-107F38A5E21540783-024010207-FS64UxyEVj6KOcLCu4fw43QZz5E6EAPYudY2CI1QvZE%3D; enable_web_push=DISABLE; home_feed_column=5; SESSDATA=f8c295b4%2C1719731563%2Cd1d4c%2A12CjDDYiSN0oQlVbstsenorLd8tEOa7N6bOlaqBgrfO4K3MaBJ-gFscdETLylqufohzEUSVkl3eWZVbnFhQVRfbU5OWExfQ0lWb1FkLVM4STFoYmxiclliOHJFWjZlSlY1Z1ZWODJkbnlDX0RWLVBsRVJCNDRjdUk1eGIzYXVLTXhUakFUNlY3VmpBIIEC; bili_jct=89d927dbb97c4b2be022d15b8b613113; DedeUserID=391293707; DedeUserID__ckMd5=c4b8c23410d7d361; sid=7ikn4k9c; header_theme_version=CLOSE; CURRENT_FNVAL=4048; browser_resolution=1512-466; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDQ0MzkxNDMsImlhdCI6MTcwNDE3OTg4MywicGx0IjotMX0.SPypSAdEq9-oiHSLtF8em-y3qPzLAIWlj-3CblukELc; bili_ticket_expires=1704439083; PVID=1'
    }
)
assert response.status_code == 200
print(response.text)
