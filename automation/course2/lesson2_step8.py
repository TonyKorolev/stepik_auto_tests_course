from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Anton")

    surname = browser.find_element(By.NAME, "lastname")
    surname.send_keys("Korolev")

    mail = browser.find_element(By.NAME, "email")
    mail.send_keys("mylo@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'ololosh.txt')
    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)
  
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()