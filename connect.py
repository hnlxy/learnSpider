import requests
import time

username = '20228019005'
password = 'lxy000000'
ip = '10.61.20.73'
ctime = int(time.time())

response = requests.get(
    # url=f'http://202.206.1.231/cgi-bin/get_challenge?callback=jQuery112408640883579229994_{ctime}&username={username}&ip={ip}&_={ctime}',
    url=f'http://[2001:da8:a400:101::231]/cgi-bin/srun_portal?callback=jQuery112409517202129668418_{ctime}&action=login&username={username}&password={password}&os=Windows+10&name=Windows&double_stack=0&chksum=e6d79063e651656c7360ee71333e1e6083e21c0b&info=%7BSRBX1%7DXydDn67vn0m6blk3%2FJB5pwH%2FSFgCmPhQBYDlUlyaP%2FaJNBhW8wP6BopMBAs4FlQseXh%2FbGEwy6ir6Zf0vlywz3l1XGE4VJLPf3mZfmiAivLrZJKJiRjkZfz1z1RbJc1C&ac_id=1&ip=&n=200&type=1&_={ctime}',
    headers={
        'Referer': 'http://202.206.1.231/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
)
print(response.text)