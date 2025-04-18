# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
import random
import string
from appium import webdriver
from locators import Languages, OnboardingPage, Course, Navigation, SettingsPage, Login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from time import sleep

# -------------------------------------------------------------------------------
# --- Fixture ---
# -------------------------------------------------------------------------------

from config import capabilities_options, appium_server_url  # Импортируем настройки

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.terminate_app("com.tradingcourses.learnhowtoinvest")
        android_driver.activate_app("com.tradingcourses.learnhowtoinvest")
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

def swipe_left(driver):
    size = driver.get_window_size()
    start_x = size['width'] * 0.8
    end_x = size['width'] * 0.2
    start_y = size['height'] / 2
    driver.swipe(start_x, start_y, end_x, start_y, 1000)

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_logout_account(driver):
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, *Languages.ENGLISH)

    # Выполняем свайпы
    for _ in range(3):
        swipe_left(driver)

    # BEGIN TRAINING
    wait_and_click(driver, *OnboardingPage.BTN_START)

    # BEGINNER COURSE
    wait_and_click(driver, *Course.BEGINNER_COURSE)

    # SETTINGS
    wait_and_click(driver, *Navigation.SETTINGS)

    # CREATE ACCOUNT
    wait_and_click(driver, *SettingsPage.BTN_CREATE_ACC)

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

    # SIGN UP
    wait_and_click(driver, *Login.BTN_SIGNIN)

    # Выбираем курс
    wait_and_click(driver, *Course.BEGINNER_COURSE)

    # SETTINGS
    wait_and_click(driver, *Navigation.SETTINGS)

    # QUIT
    wait_and_click(driver, *SettingsPage.QUIT)

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------