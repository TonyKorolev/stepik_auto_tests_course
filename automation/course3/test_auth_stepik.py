import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time

final = ""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(final)

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899",
    "236903", "236904", "236905"])
# @pytest.mark.parametrize('lesson', ["236895"])
def test_auth(browser, lesson):
    global final
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.implicitly_wait(10)
    browser.get(link)
    
    button = browser.find_element(By.ID, "ember33")
    # button = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.ID, "ember33")))
    button.click()
    
    time.sleep(2)
    input_email = browser.find_element(By.ID, "id_login_email")
    input_email.send_keys("antoshka.992@mail.ru")

    input_pass = browser.find_element(By.ID, "id_login_password")
    input_pass.send_keys("*******")

    button_form = browser.find_element(By.CLASS_NAME, "sign-form__btn")
    button_form.click()

    time.sleep(3)
    # input_answer = WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea")))
    input_answer = browser.find_element(By.CSS_SELECTOR, "textarea")
    input_answer.send_keys(str(math.log(int(time.time()))))
    
    time.sleep(3)
    button_enter = browser.find_element(By.CLASS_NAME, "submit-submission")
    # button_enter = WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    button_enter.click()
    
    time.sleep(3)
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    # is_message_correct = WebDriverWait(browser, 5).until(EC.visibility_of((By.CLASS_NAME, "ember_application")))
    # if is_message_correct != True:
    try:
        assert "Correct!" == message, "Answer in not correct!"
    except AssertionError:
        final += message