import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

link = 'https://suninjuly.github.io/registration1.html'
link2 = 'https://suninjuly.github.io/registration2.html'


def test_register(url):
    browser = webdriver.Chrome()
    browser.get(url)

    input_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class input')
    input_name.send_keys('Konstantin')

    input_last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class input')
    input_last_name.send_keys('Stolyarov')

    input_email = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class input')
    input_email.send_keys('sk7konstantin@yandex.ru')

    input_phone = browser.find_element(By.CSS_SELECTOR, '.second_block .first_class input')
    input_phone.send_keys('8-900-927-87-78')

    input_address = browser.find_element(By.CSS_SELECTOR, '.second_block .second_class input')
    input_address.send_keys('Sankt-Petersburg')

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    time.sleep(0.5)

    h1_text = browser.find_element(By.TAG_NAME, 'h1').text

    browser.quit()

    return h1_text


class TestRegister(unittest.TestCase):
    def test2(self):
        self.assertEqual(test_register(link2), 'Congratulations! You have successfully registered!', 'Ошибка в тесте 2')
    def test1(self):
        self.assertEqual(test_register(link), 'Congratulations! You have successfully registered!', 'Ошибка в тесте 1')


if __name__ == '__main__':
    unittest.main()
