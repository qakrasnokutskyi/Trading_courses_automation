# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
import random
import string
from time import sleep
from faker import Faker
from appium import webdriver
from locators import Languages,Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------------------------------------------------------------------------------
# --- Fixture ---
# -------------------------------------------------------------------------------

from config import capabilities_options, appium_server_url  # Импортируем настройки

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.quit()

# -------------------------------------------------------------------------------
# --- Utils ---
# -------------------------------------------------------------------------------

# Создаем экземпляр Faker для генерации данных
fake = Faker()

def generate_random_password(length=10):
    # Генерация случайного пароля с латинскими буквами и цифрами
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def wait_and_click(driver, by, value, timeout=10):
    """Ожидание элемента и клик."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_register_empty_fields(driver):
    sleep(7)

    # English Language
    wait_and_click(driver, *Languages.ENGLISH)

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, *Login.BTN_REGISTRATION_LOGIN)

    # Переходим в раздел "Регистрация"
    wait_and_click(driver, *Login.PAGE_REGISTRATION)

    # Заполняем поле Имя
    name = wait_for_element(driver, *Login.FIELD_NAME)
    name.send_keys('')

    # Заполняем поле Email
    email = wait_for_element(driver, *Login.FIELD_EMAIL)
    email.send_keys('')

    # Заполняем поле Password
    password = wait_for_element(driver, *Login.FIELD_PASSWORD)
    password.send_keys('')

    # Заходим в новый аккаунт
    wait_and_click(driver, *Login.BTN_SIGNIN)

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------

    registration_page_login = wait_for_element(driver, *Login.PAGE_LOGIN)
    assert registration_page_login is not None, 'Раздел "Логин" не отобразился'

    registration_page_registration = wait_for_element(driver, *Login.PAGE_REGISTRATION)
    assert registration_page_registration is not None,'Раздел "Регистрация" не отобразился'

    logo_app = wait_for_element(driver, *Login.LOGO_APPLICATION)
    assert logo_app is not None,'Лого раздела не отобразился'