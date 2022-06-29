from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
path = "C:\Development\chromedriver.exe"

s = Service(executable_path=path)

driver = webdriver.Chrome(service=s)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&geoId=101174742&keywords=python%20developer&location=Canada")
driver.maximize_window()
sign_in_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in_button.click()

username = driver.find_element(By.ID, "username")
username.send_keys(USERNAME)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

sign_in = driver.find_element(By.CLASS_NAME, "from__button--floating")
sign_in.click()

save_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list li")
save_ids = [save_item.get_attribute("id") for save_item in save_list]

for item in save_ids:
    if item == '':
        continue
    else:
        save = driver.find_element(By.ID, item)
        save.click()

        save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_button.click()
        time.sleep(1)