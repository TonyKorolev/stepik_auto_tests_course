from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestFormRegistration(unittest.TestCase):
    
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # labels = browser.find_elements

        input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        input1.send_keys("Anton")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        input2.send_keys("Korolev")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
        input3.send_keys("mylo@mail.com")
        time.sleep(3)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Expected resualt is not equal actual!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # labels = browser.find_elements

        input1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
        input1.send_keys("Anton")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
        input2.send_keys("Korolev")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
        input3.send_keys("mylo@mail.com")
        time.sleep(3)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Expected resualt is not equal actual!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()
    