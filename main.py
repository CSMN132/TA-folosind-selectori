import email
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://automationintesting.online")

name_input = driver.find_element(By.ID, 'name')
name_input.send_keys("Jonathan")

time.sleep(1)

email_input = driver.find_element(By.ID, 'email')
email_input.send_keys("test@gmail.com")

time.sleep(1)

phone_input = driver.find_element(By.ID, 'phone')
phone_input.send_keys("084671268124")

time.sleep(1)

subject_input = driver.find_element(By.ID, 'subject')
subject_input.send_keys("TestTest")

time.sleep(1)

subject_input = driver.find_element(By.ID, 'description')
subject_input.send_keys("acesta este un test pentru a vedea daca functioneaza codul")

time.sleep(5)

submitcontact_button = driver.find_element(By.ID, 'submitContact')
submitcontact_button.click()

time.sleep(5)
