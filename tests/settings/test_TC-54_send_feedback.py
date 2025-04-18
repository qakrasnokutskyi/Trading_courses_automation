# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
import random
import string
from appium import webdriver
from locators import Languages, Login, Navigation, BrokerPage, OnboardingPage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def wait_and_click(driver, by, value, timeout=10):
    """Ожидание элемента и клик."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_send_feedback(driver):
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, *Languages.ENGLISH)

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, *Login.BTN_REGISTRATION_LOGIN)

    # Заполняем поле email
    email = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Your email")')
    email.send_keys('qakrasnokutskiy@gmail.com')
    sleep(1)

    # Заполняем поле password
    password = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Your password")')
    password.send_keys('e251dq12r')
    sleep(1)

    # Выполняем вход
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_signIn")')

    # SETTINGS
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/settings")')

    # Отправляем отзыв через экран "Настройки"
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Send Feedback")')

    # Генерируем случайный текст
    random_text = ''.join(
    random.choices(string.ascii_letters + string.digits + ' ', k=50))  # Случайный текст длиной 50 символов

    # Находим поле ввода и вводим случайный текст
    input_field = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText')
    input_field.send_keys(random_text)
    sleep(1)

    print(f"Случайный текст успешно введен: {random_text}")

    #Отправляем отзыв
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_send")')

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------