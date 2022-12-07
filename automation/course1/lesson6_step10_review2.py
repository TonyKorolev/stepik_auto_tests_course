from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    First_name = browser.find_element(By.CSS_SELECTOR,
                                      "div.first_block>div.form-group.first_class>input.form-control.first")
    Second_name = browser.find_element(By.CSS_SELECTOR,
                                       "div.first_block>div.form-group.second_class>input.form-control.second")
    mail = browser.find_element(By.CSS_SELECTOR, "div.first_block>div.form-group.third_class>input.form-control.third")

    First_name.send_keys("name")
    Second_name.send_keys("Last_name")
    mail.send_keys("mail")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)

    browser.quit()
