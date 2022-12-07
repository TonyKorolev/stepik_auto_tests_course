from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()
    
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Anton")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Korolev")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.city")
    input3.send_keys("Cheboksary")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
