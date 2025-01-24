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

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency"]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    btc = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency" and @text="BTC/USD"]')
    btc.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency"]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    chf = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency" and @text="CHF/USD"]')
    chf.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency"]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    eur = driver.find_element(By.XPATH, '(//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency"])[5]')
    eur.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency"]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    jpy = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency" and @text="JPY/USD"]')
    jpy.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency"]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    nzd = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency" and @text="NZD/USD"]')
    nzd.click()
    sleep(2)

    # Открываем список валютных пар
    pairs = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency"]')
    pairs.click()
    sleep(1)

    # Переключаем на другую валютную пару
    rub = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_currency" and @text="RUB/USD"]')
    rub.click()
    sleep(2)



