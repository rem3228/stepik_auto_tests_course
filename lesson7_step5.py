from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'
driver = webdriver.Chrome()

try:
    driver.get(link)
    x = float(driver.find_element(By.XPATH, "//span[@id='input_value']").text)

    text_area = driver.find_element(By.XPATH, "//input[@id='answer']")
    text_area.send_keys(str(calc(x)))

    checkbox = driver.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    checkbox.click()

    radio = driver.find_element(By.XPATH, "//input[@id='robotsRule']")
    radio.click()

    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
finally:
    time.sleep(10)
    driver.quit()
