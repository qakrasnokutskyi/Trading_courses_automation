# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
import random
import string
from config import capabilities_options, appium_server_url  # Импортируем настройки
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

from locators import Languages, OnboardingPage, Course, Navigation, SettingsPage, Login, TrainingPage, MainPage


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

def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_switch_course_from_settings(driver):
    sleep(7)

    # English Language
    wait_and_click(driver, *Languages.ENGLISH)

    # Выполняем свайпы
    for _ in range(3):
        swipe_left(driver)

    #Нажимаем кнопку "BEGIN TRAINING"
    wait_and_click(driver, *OnboardingPage.BTN_START)

    #Выбираем "Про+ курс"
    wait_and_click(driver, *Course.PRO_COURSE)

    #Переходим в создать аккаунт
    wait_and_click(driver, *Navigation.SETTINGS)
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

    # Заходим в новый аккаунт
    wait_and_click(driver, *Login.BTN_SIGNIN)

    #Выбираем начальный курс
    wait_and_click(driver, *Course.BEGINNER_COURSE)

    # Переходим в раздел "Обучение" для смены курса
    wait_and_click(driver, *Navigation.TRAINING)

    # Выбираем новый курс
    wait_and_click(driver, *TrainingPage.CHANGE_COURSE)
    wait_and_click(driver, *Course.BEGINNER_COURSE)

    wait_and_click(driver, *TrainingPage.CHANGE_COURSE)
    wait_and_click(driver, *Course.MIDDLE_COURSE)

    wait_and_click(driver, *TrainingPage.CHANGE_COURSE)
    wait_and_click(driver, *Course.ADVANCED_COURSE)

    wait_and_click(driver, *TrainingPage.CHANGE_COURSE)
    wait_and_click(driver, *Course.PRO_COURSE)

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------

    demo_balance = wait_for_element(driver, *MainPage.DEMO_BALANCE)
    assert demo_balance is not None, 'Demo balance is not found'

    change_course_btn = wait_for_element(driver, *TrainingPage.CHANGE_COURSE)
    assert change_course_btn is not None, 'Change course button is not found'

    navigation_training = wait_for_element(driver, *Navigation.TRAINING)
    assert navigation_training is not None, 'Navigation training is not found'

    navigation_trading = wait_for_element(driver, *Navigation.TRADING)
    assert navigation_trading is not None, 'Navigation trading is not found'

    navigation_broker = wait_for_element(driver, *Navigation.BROKERS)
    assert navigation_broker is not None, 'Navigation broker is not found'

    navigation_settings = wait_for_element(driver, *Navigation.SETTINGS)
    assert navigation_settings is not None, 'Navigation settings is not found'