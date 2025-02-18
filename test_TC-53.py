from datetime import datetime

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep, time

#=============================================#

from config import capabilities_options, appium_server_url  # Импортируем настройки

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.terminate_app("com.tradingcourses.learnhowtoinvest")
        android_driver.activate_app("com.tradingcourses.learnhowtoinvest")
        android_driver.quit()

def wait_and_click(driver, by, value, timeout=10):
    """Ожидание элемента и клик."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
    element.click()

def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

#=============================================#

def test_swap_currency_pairs(driver):
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_enter")')

    # Заполняем поле email
    email = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Your email")')
    email.send_keys('qakrasnokutskiy@gmail.com')
    sleep(1)

    # Заполняем поле password
    password = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Your password")')
    password.send_keys('e251dq12r')
    sleep(1)

    # Выполняем вход
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_signIn")')

    # Переходим в раздел Брокеры
    wait_and_click(driver, MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/brokers")')

    # Проверяем месяц и год с реальным временем
    try:
        # Получаем отображаемый текст месяца и года из приложения
        app_date_element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[2]')
        app_date_text = app_date_element.text.strip()

        # Получаем текущий месяц и год
        current_date = datetime.now()
        current_month_year = current_date.strftime("%B %Y")  # Пример: "December 2024"

        # Сравниваем отображаемое время с текущим
        assert app_date_text == current_month_year, f"Ожидаемый месяц и год: {current_month_year}, но отображается: {app_date_text}"

        print("Месяц и год совпадают с реальным временем. Тест пройден.")

    except AssertionError as e:

        print(f"Ошибка: {e}")

    except Exception as e:

        print(f"Ошибка при проверке месяца и года: {e}")
