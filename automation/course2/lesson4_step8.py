from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    if price == True:
        button.click()

    x_input = browser.find_element(By.ID, "input_value")
    x = int(x_input.text)
    y = math.log(abs(12 * math.sin(x)))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button_captcha = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_captcha)
    button_captcha.click()

finally:
    time.sleep(20)
    browser.quit()