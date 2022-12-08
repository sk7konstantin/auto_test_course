import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


links = ['https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('link', links)
class TestAuth:
    correct_answer = 'Correct!'

    def test_auth_and_send_answer(self, browser, link):
        browser.get(link)
        browser.implicitly_wait(5)
        print('-----start_auth-----')
        try:
            browser.find_element(By.ID, 'ember33').click()
            browser.find_element(By.CSS_SELECTOR, 'input#id_login_email').send_keys('faken@mail.ru')
            browser.find_element(By.CSS_SELECTOR, 'input#id_login_password').send_keys('s232342')
            browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader ').click()
        except Exception:
            pass

        try:
            button_again = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'again-btn'))
            )
            button_again.click()
        except Exception:
            pass

        time.sleep(2)
        input = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea'))
        )
        answer = math.log(int(time.time()))
        input.send_keys(str(answer))


        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))
        ).click()

        text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
        ).text

        assert text == self.correct_answer, f'{text}'
        time.sleep(1)


    