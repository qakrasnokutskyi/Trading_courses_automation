import pytest
import random
import string
from time import sleep, time
from faker import Faker
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

#=============================================#


def test_registration(driver):
    sleep(7)

    # English Language
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_enter")')

    # Переходим в раздел "Регистрация"
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_tab_reg")')

    # Генерируем случайные значения для полей
    random_name = fake.first_name()
    random_password = generate_random_password()

    # Заполняем поле Имя
    name = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your name"]')
    name.send_keys(random_name)
    sleep(1)

    # Заполняем поле Email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys('qwerty123')
    sleep(1)

    # Заполняем поле Password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys(random_password)
    sleep(1)

    # Заходим в новый аккаунт
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_signIn")')
