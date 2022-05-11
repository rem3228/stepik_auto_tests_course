import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://SunInJuly.github.io/execute_script.html'
driver = webdriver.Chrome()

try:
    driver.get(link)
    x = driver.find_element(By.XPATH, "//span[@id='input_value']").text
    text_area = driver.find_element(By.XPATH, "//input[@id='answer']")
    text_area.send_keys(calc(x))
    checkbox = driver.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    checkbox.click()
    radio = driver.find_element(By.XPATH, "//input[@id='robotsRule']")
    driver.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
finally:
    time.sleep(10)
    driver.quit()
