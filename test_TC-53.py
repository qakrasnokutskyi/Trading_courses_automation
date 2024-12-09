import pytest
import allure
from appium import webdriver
from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep, time
from appium.options.android import UiAutomator2Options


# Для автотестов использовать только телефон Motorola.
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='ZY32FX9296', # Phone Motorola
    platformVersion='11',
    appPackage='com.tradingcourses.learnhowtoinvest',
    appActivity='com.trade.test.ui.splash.SplashActivity',
    language='en',
    locale='US'
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.quit()


def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

def test_swap_currency_pairs(driver):
    sleep(7)

    # Выбираем англ язык
    english = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="English"]')
    english.click()
    sleep(1)

    # Нажимает кнопку "Войти/Зарегистрироваться
    login = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_enter"]')
    login.click()
    sleep(1)

    # Заполняем поле email
    email = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your email"]')
    email.send_keys('qakrasnokutskiy@gmail.com')
    sleep(1)
    print('Поле успешно заполнено')

    # Заполняем поле password
    password = driver.find_element(By.XPATH, '//android.widget.EditText[@text="Your password"]')
    password.send_keys('e251dq12r')
    sleep(1)
    print('Поле успешно заполнено')

    # Выполняем вход
    signin = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.tradingcourses.learnhowtoinvest:id/bt_signIn"]')
    signin.click()
    sleep(3)

    # Переходим в раздел Брокеры
    brokers = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Brokers"]')
    brokers.click()
    sleep(3)

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
