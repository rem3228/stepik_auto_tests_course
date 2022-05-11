from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
driver = webdriver.Chrome()

try:
    driver.get(link)
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    time.sleep(2)
    second_window = driver.window_handles[1]
    driver.switch_to.window(second_window)
    x = driver.find_element(By.ID, "input_value").text
    text_area = driver.find_element(By.NAME, "text")
    text_area.send_keys(calc(x))
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    alert = driver.switch_to.alert
    print(alert.text.split(":")[-1].strip())
finally:
    driver.quit()
