import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import capabilities_options, appium_server_url

# ==================== fixture ====================

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    android_driver.quit()

# ==================== Utilits ====================

def wait_and_click(driver, by, value, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# ==================== Selectors ====================

LANGUAGE_ENGLISH = 'new UiSelector().text("English")'
BTN_SIGN_IN = 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_enter")'
FIELD_EMAIL_XPATH = '//android.widget.EditText[@text="Your email"]'
FIELD_PASSWORD_XPATH = '//android.widget.EditText[@text="Your password"]'
BTN_SUBMIT = 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_signIn")'
BTN_SETTINGS = 'new UiSelector().text("Settings")'

# ==================== Test ====================

def test_login_valid(driver):
    # Выбираем английский
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, LANGUAGE_ENGLISH)

    # Переход на экран логина
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, BTN_SIGN_IN)

    # Ввод email
    email_field = wait_for_element(driver, AppiumBy.XPATH, FIELD_EMAIL_XPATH)
    email_field.send_keys('qakrasnokutskiy@gmail.com')

    # Ввод пароля
    password_field = wait_for_element(driver, AppiumBy.XPATH, FIELD_PASSWORD_XPATH)
    password_field.send_keys('e251dq12r')

    # Нажимаем «войти»
    wait_and_click(driver, AppiumBy.ANDROID_UIAUTOMATOR, BTN_SUBMIT)

    # Проверка: попали на экран с кнопкой "Settings"
    settings_btn = wait_for_element(driver, AppiumBy.ANDROID_UIAUTOMATOR, BTN_SETTINGS)
    assert settings_btn is not None, "❌ Кнопка 'Settings' не найдена — вход, не удался"
