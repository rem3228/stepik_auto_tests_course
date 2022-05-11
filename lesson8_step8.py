from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
link = 'https://suninjuly.github.io/file_input.html'
driver = webdriver.Chrome()

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    driver.get(link)
    name = driver.find_element(By.NAME, "firstname")
    last_name = driver.find_element(By.NAME, "lastname")
    mail = driver.find_element(By.NAME,"email")
    file = driver.find_element(By.NAME, "file")
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    name.send_keys("Jo")
    last_name.send_keys("Jo")
    mail.send_keys("JoJo@mail.ru")
    file.send_keys(file_path)
    submit.click()


finally:
    time.sleep(10)
    driver.quit()