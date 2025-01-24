import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#=============================================#

from config import capabilities_options, appium_server_url  # Импортируем настройки

@pytest.fixture(scope="function")
def driver():
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield android_driver
    android_driver.quit()


def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

#=============================================#

def test_change_language(driver):
    sleep(7)

    # Выбираем Украинский язык
    english = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="English"]')
    english.click()
    sleep(1)

    # Проходим онбоард экран
    begin_trading = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.tradingcourses.learnhowtoinvest:id/bt_start"]')
    begin_trading.click()
    sleep(1)

    # Выбираем курс
    begin = driver.find_element(By.XPATH, '//android.view.ViewGroup[@resource-id="com.tradingcourses.learnhowtoinvest:id/ll_beginner"]')
    begin.click()
    sleep(1)

