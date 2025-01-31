import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.fetch import continue_request

driver = webdriver.Chrome()
url = "https://www.divan.ru/ekaterinburg/category/svet"
driver.get(url)
time.sleep(3)

svets = driver.find_elements(By.CSS_SELECTOR, 'div._Ud0k')

parsed_data = []

for svet in svets:
    try:
        title = svet.find_element(By.CSS_SELECTOR, 'div.lsooF').text
        price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2').text
        link = svet.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue

        parsed_data.append([title, price, link])
driver.quit()

with open("svet_divan.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'Цена', 'Ссылка на светильник'])
    writer.writerows(parsed_data)