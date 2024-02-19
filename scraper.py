# open_google.py

# Dependencies
# First install pip install selenium
# pip install webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com")  # Corrected the URL to google.com
driver.maximize_window()

# search input path
user_input = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys('https://www.glassdoor.co.in/Reviews/index.htm')
time.sleep(2)

user_input.send_keys(Keys.ENTER)
time.sleep(2)


link = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/span/a/h3')
link.click()


# try:
#     with open('all_pages_source.html', 'w', encoding='utf-8') as file:
#         for i in range(500):
#             l2 = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[3]/div[1]/div[4]/div[3]/div/div/div[1]/button[7]')
#             l2.click()
#             time.sleep(2)

#             file.write(driver.page_source)
#             file.write('\n\n')
# except:
#     pass

 

try:
    for i in range(500):
        l2 = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[3]/div[1]/div[4]/div[3]/div/div/div[1]/button[7]')
        l2.click()
        time.sleep(2)

        file_name = f'page_{i+1}_source.html'
        
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

except Exception as e:
    print(f"An error occurred: {e}")


