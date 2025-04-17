# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Languages,Login,MainPage

from config import capabilities_options, appium_server_url

# -------------------------------------------------------------------------------
# --- Fixture ---
# -------------------------------------------------------------------------------

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    android_driver.quit()

# -------------------------------------------------------------------------------
# --- Utils ---
# -------------------------------------------------------------------------------

def wait_and_click(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_login_valid(driver):
    # Выбираем английский
    wait_and_click(driver, *Languages.ENGLISH)

    # Переход на экран логина
    wait_and_click(driver, *Login.BTN_REGISTRATION_LOGIN)

    # Ввод email
    email_field = wait_for_element(driver, *Login.FIELD_EMAIL)
    email_field.send_keys('qakrasnokutskiy@gmail.com')

    # Ввод пароля
    password_field = wait_for_element(driver, *Login.FIELD_PASSWORD)
    password_field.send_keys('e251dq12r')

    # Нажимаем «войти»
    wait_and_click(driver, *Login.BTN_SIGNIN)

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------
    your_balance = wait_for_element(driver, *MainPage.DEMO_BALANCE)
    assert your_balance is not None, "Поле 'Your balance' не отображается!"

    change_course = wait_for_element(driver, *MainPage.CHANGE_COURSE)
    assert change_course is not None, "Кнопки 'Изменить курс' не найдено!"

