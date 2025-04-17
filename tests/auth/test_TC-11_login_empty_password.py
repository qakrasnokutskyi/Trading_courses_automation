import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from time import sleep

from locators import Languages,Login

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#=============================================#

from config import capabilities_options, appium_server_url  # Импортируем настройки

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    android_driver.quit()

def wait_and_click(driver, by, value, timeout=10):
    """Ожидание элемента и клик."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

#=============================================#

def test_login_empty_password(driver):
    sleep(7)

    # English Language
    wait_and_click(driver, *Languages.ENGLISH)

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, *Login.BTN_REGISTRATION_LOGIN)

    # Заполняем поле email
    email_field = wait_for_element(driver, *Login.FIELD_EMAIL)
    email_field.send_keys('qakrasnokutskiy@gmail.com')

    # Заполняем поле password
    password_field = wait_for_element(driver, *Login.FIELD_PASSWORD)
    password_field.send_keys('')

    # Выполняем вход
    wait_and_click(driver, *Login.BTN_SIGNIN)

# ==================== asserts ====================

    registration_page_login = wait_for_element(driver, *Login.PAGE_LOGIN)
    assert registration_page_login is not None, 'Раздел "Логин" не отобразился'

    registration_page_registration = wait_for_element(driver, *Login.PAGE_REGISTRATION)
    assert registration_page_registration is not None,'Раздел "Регистрация" не отобразился'

    logo_app = wait_for_element(driver, *Login.LOGO_APPLICATION)
    assert logo_app is not None,'Лого раздела не отобразился'