from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num1 = int(num1_element.text)
    num2_element = browser.find_element(By.ID, "num2")
    num2 = int(num2_element.text)
    sum = num1 + num2

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sum))

    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
