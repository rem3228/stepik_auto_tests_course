import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

link = 'https://suninjuly.github.io/selects1.html'

driver = webdriver.Chrome()

try:
    driver.get(link)

    num1 = int(driver.find_element(By.XPATH, "//span[@id='num1']").text)
    num2 = int(driver.find_element(By.XPATH, "//span[@id='num2']").text)
    select = Select(driver.find_element(By.XPATH, "//select[@class='custom-select']"))
    select.select_by_value(str(num1 + num2))
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
finally:
    time.sleep(10)
    driver.quit()
