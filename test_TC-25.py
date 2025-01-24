import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time

#=============================================#

from config import capabilities_options, appium_server_url  # Импортируем настройки

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    if android_driver:
        android_driver.quit()


def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

#=============================================#

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

    # Переходим на экран c графиком
    trading = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Trading"]')
    trading.click()
    sleep(1)

    # Открываем "Таймфрейм"
    timeframe = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/iv_timeframe"]')
    timeframe.click()
    sleep(2)

    # Выбираем таймфрейм "S20"
    s20 = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_s20"]')
    s20.click()
    sleep(3)

    # Открываем "Таймфрейм"
    timeframe = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/iv_timeframe"]')
    timeframe.click()
    sleep(2)

    # Выбираем таймфрейм "m1"
    m1 = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_m1"]')
    m1.click()
    sleep(3)

    # Открываем "Таймфрейм"
    timeframe = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/iv_timeframe"]')
    timeframe.click()
    sleep(2)

    # Выбираем таймфрейм "m2"
    m2 = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_m2"]')
    m2.click()
    sleep(3)
