from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    input_answer.send_keys(y)

    # time.sleep(1)

    checkbox_option = browser.find_element(By.ID, "robotCheckbox")
    checkbox_option.click()

    # time.sleep(1)

    radio_option = browser.find_element(By.ID, "robotsRule")
    radio_option.click()

    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()