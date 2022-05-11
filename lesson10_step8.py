import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

driver = webdriver.Chrome()

try:
    driver.get(link)
    WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = driver.find_element(By.ID, "book")
    button.click()
    x = driver.find_element(By.ID, "input_value").text
    text_area = driver.find_element(By.NAME, "text")
    text_area.send_keys(calc(x))
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    alert = driver.switch_to.alert
    print(alert.text.split(":")[-1].strip())
finally:
    driver.quit()