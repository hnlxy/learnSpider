import requests
import ddddocr

# 获得验证码网址
generate_response = requests.post('https://api.ruanwen.la/api/auth/captcha/generate')
# generate_response_cookies = generate_response.cookies.get_dict()
captcha_token = generate_response.json()['data']['captcha_token']
# print(captcha_token)

# 识别验证码
captcha_response = requests.get(
    url=generate_response.json()['data']['src'],
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    }
)
# print(captcha_response.content)
# with open('.\\imgs\\captcha.jpg', 'wb') as f:
#     f.write(captcha_response.content)

ocr = ddddocr.DdddOcr(show_ad=False)
captcha = ocr.classification(captcha_response.content)
print(captcha)

# 登录
authenticate_response = requests.post(
    url='https://api.ruanwen.la/api/auth/authenticate',
    json={"mobile":"15539482823","device":"pc","password":"lxy000000","captcha_token":captcha_token,"captcha":captcha,"identity":"advertiser"},
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT',
        'Content-Type': 'application/json;charset=UTF-8'
    }
)
print(authenticate_response.text)
