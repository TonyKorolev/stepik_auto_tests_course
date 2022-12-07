from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "img[valuex]")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()