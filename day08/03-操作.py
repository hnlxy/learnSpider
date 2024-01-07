import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('chromedriver-win64/chromedriver.exe')
driver = Chrome(service=service)
driver.get('https://passport.bilibili.com/login?gourl=https%3A%2F%2Fpassport.bilibili.com%2Faccount%2Fsecurity%23%2Fhome')

time.sleep(2)
sms_login_btn = driver.find_element(By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]')
sms_login_btn.click()

time.sleep(2)
phone_input = driver.find_element(By.XPATH, value='//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input')
phone_input.send_keys('15539482823')

time.sleep(10)
driver.close()