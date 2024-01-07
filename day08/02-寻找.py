import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='chromedriver-win64/chromedriver.exe')
driver = Chrome(service=service)
driver.get('https://www.5xclass.cn/')

# /html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/strong
# /html/body/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div/strong
root_tag = driver.find_element(By.TAG_NAME, value='html')
ul_tag = root_tag.find_element(By.CLASS_NAME, value='list')
for li in ul_tag.find_elements(By.TAG_NAME, 'li'):
    print(li.find_element(By.TAG_NAME, value='a').text)

time.sleep(100)
print(driver)