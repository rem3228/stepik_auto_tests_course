import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = 'http://suninjuly.github.io/find_link_text'
driver = webdriver.Chrome()


try:
    driver.get(link)
    href = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    href.click()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'timer')))

    input1 = driver.find_elements(by=By.TAG_NAME, value="input")[0]
    input1.send_keys("Ivan")
    input2 = driver.find_element(by=By.NAME, value="last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(by=By.CLASS_NAME, value="city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(by=By.ID, value="country")
    input4.send_keys("Russia")
    button = driver.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()
finally:
    time.sleep(10)
    driver.close()
