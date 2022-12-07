from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    
    new_window_name = browser.window_handles[1]
    new_window = browser.switch_to.window(new_window_name)
    
    x_input = browser.find_element(By.ID, "input_value")
    x = int(x_input.text)
    y = math.log(abs(12 * math.sin(x)))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button_captcha = browser.find_element(By.CLASS_NAME, "btn")
    button_captcha.click()

finally:
    time.sleep(20)
    browser.quit()
