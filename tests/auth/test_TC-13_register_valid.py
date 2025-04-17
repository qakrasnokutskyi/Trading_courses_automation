import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Languages, Login, Course, Navigation, SettingsPage

from time import sleep, time
from faker import Faker
import random
import string

#=============================================#

# Создаем экземпляр Faker для генерации данных
fake = Faker()

def generate_random_password(length=10):
    # Генерация случайного пароля с латинскими буквами и цифрами
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

#=============================================#

#=============================================#

from config import capabilities_options, appium_server_url  # Импортируем настройки

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.quit()

def wait_and_click(driver, by, value, timeout=10):
    """Ожидание элемента и клик."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

#=============================================#

def test_register_valid(driver):
    sleep(7)

    # English Language
    wait_and_click(driver, *Languages.ENGLISH)

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, *Login.BTN_REGISTRATION_LOGIN)

    # Переходим в раздел "Регистрация"
    wait_and_click(driver, *Login.PAGE_REGISTRATION)

    # Генерируем случайные значения для полей
    random_name = fake.first_name()
    random_email = fake.email()
    random_password = generate_random_password()

    # Заполняем поле Имя
    name = wait_for_element(driver, *Login.FIELD_NAME)
    name.send_keys(random_name)

    # Заполняем поле Email
    email = wait_for_element(driver, *Login.FIELD_EMAIL)
    email.send_keys(random_email)

    # Заполняем поле Password
    password = wait_for_element(driver, *Login.FIELD_PASSWORD)
    password.send_keys(random_password)

    # Заходим в новый аккаунт
    wait_and_click(driver, *Login.BTN_SIGNIN)

    # Выбираем курс
    wait_and_click(driver, *Course.BEGINNER_COURSE)

    # Переходим в настройки
    wait_and_click(driver, *Navigation.SETTINGS)

# ==================== asserts ====================

    settings_page = wait_for_element(driver, *SettingsPage.SETTINGS_TITLE)
    assert settings_page is not None,'Поле не отображается'

    email_user = wait_for_element(driver, *SettingsPage.USER_EMAIL)
    assert email_user is not None,'Поле не отобразилось'

    change_language = wait_for_element(driver, *SettingsPage.CHANGE_LANGUAGE)
    assert change_language is not None, 'Поле не отобразилось'

    send_feedback = wait_for_element(driver, *SettingsPage.SEND_FEEDBACK)
    assert send_feedback is not None, 'Поле не отобразилось'

    rate_us = wait_for_element(driver, *SettingsPage.RATE_US)
    assert rate_us is not None,'Поле не отобразилось'

    quit_user = wait_for_element(driver, *SettingsPage.QUIT)
    assert quit_user is not None, 'Поле не отобразилось'
