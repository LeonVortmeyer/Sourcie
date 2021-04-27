from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv
import pandas as pd

username = 'username'
password = 'password'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://www.linkedin.com/login')


driver.implicitly_wait(10)

email_field_xpath = '//*[@id="username"]'
password_field_xpath = '//*[@id="password"]'

email_field = driver.find_element_by_xpath(email_field_xpath)
email_field.click()
email_field.send_keys(username)

password_field = driver.find_element_by_xpath(password_field_xpath)
password_field.click()
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)
driver.implicitly_wait(1)

driver.get('https://www.linkedin.com/in/ed-authur-425ab89')


