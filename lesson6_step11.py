from selenium import webdriver
from selenium.webdriver.common.by import By

import time

link = "https://suninjuly.github.io/registration2.html"

browser = webdriver.Chrome()


try:

    browser.get(link)

    input1 = browser.find_element(by=By.XPATH,
                                                  value="//div[@class='first_block']/div[@class='form-group first_class']/input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(by=By.XPATH,
                                                  value="//div[@class='first_block']/div[@class='form-group second_class']/input")
    input2.send_keys("Petrov")
    input3 = browser.find_element(by=By.XPATH,
                                                  value="//div[@class='first_block']/div[@class='form-group third_class']/input")
    input3.send_keys("mail@mail.com")
    input4 = browser.find_element(by=By.XPATH,
                                                  value="//div[@class='second_block']/div[@class='form-group first_class']/input")
    input4.send_keys("+7545615")
    input5 = browser.find_element(by=By.XPATH,
                                                  value="//div[@class='second_block']/div[@class='form-group second_class']/input")
    input5.send_keys("Russia")
    button = browser.find_element(by=By.XPATH, value="//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()


