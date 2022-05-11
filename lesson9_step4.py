import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'

try:
    driver.get(link)
    btn = driver.find_element(By.TAG_NAME, 'button')
    btn.click()
    confirm = driver.switch_to.alert
    confirm.accept()
    time.sleep(2)
    x = driver.find_element(By.ID, "input_value").text
    text_area = driver.find_element(By.NAME, "text")
    text_area.send_keys(calc(x))
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    alert = driver.switch_to.alert
    print(alert.text.split(":")[-1].strip())
finally:
    driver.quit()
