import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service = Service('chromedriver-win64/chromedriver.exe')
driver = Chrome(service=service)

driver.get(
    'https://passport.bilibili.com/login?gourl=https%3A%2F%2Fpassport.bilibili.com%2Faccount%2Fsecurity%23%2Fhome')


# lambda等待
# sms_btn = WebDriverWait(driver, 10, 0.5).until(
#     lambda dv: dv.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]'))
# sms_btn.click()


# 函数等待
# def wait_func(dv):
#     tag = dv.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]')
#     return tag
#
#
# sms_btn = WebDriverWait(driver, 10, 0.5).until(wait_func)
# sms_btn.click()

# 全部动作应用
driver.implicitly_wait(10)
sms_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[1]/div[3]')
sms_btn.click()

time.sleep(2)
driver.quit()
