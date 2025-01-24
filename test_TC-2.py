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

def test_change_language(driver):
    sleep(7)

    # Выбираем англ язык
    english = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="English"]')
    english.click()
    sleep(1)

    # Проходи анбоард экран
    begin_trading = driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.tradingcourses.learnhowtoinvest:id/bt_start"]')
    begin_trading.click()
    sleep(1)

    # Выбираем курс
    begin = driver.find_element(By.XPATH, '//android.view.ViewGroup[@resource-id="com.tradingcourses.learnhowtoinvest:id/ll_beginner"]')
    begin.click()
    sleep(1)

    # Переходим в настройки
    settings = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Settings"]')
    settings.click()
    sleep(1)

    # Выбираем смену языка
    change_language = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_lang_label"]')
    change_language.click()
    sleep(1)

    # Выбираем Русский язык
    russian = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="Русский"]')
    russian.click()
    sleep(1)

    # Переходим в настройки
    settings = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Настройки"]')
    settings.click()
    sleep(1)

    # Выбираем смену языка
    change_language = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_lang_label"]')
    change_language.click()
    sleep(1)

    # Выбираем Украинский язык
    ukraine = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="Українська"]')
    ukraine.click()
    sleep(1)

    # Переходим в настройки
    settings = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Налаштування"]')
    settings.click()
    sleep(1)

    # Выбираем смену языка
    change_language = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_lang_label"]')
    change_language.click()
    sleep(1)

    # Выбираем Немецкий язык
    deutsch = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="Deutsch"]')
    deutsch.click()
    sleep(1)

    # Переходим в настройки
    settings = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Einstellungen"]')
    settings.click()
    sleep(1)

    # Выбираем смену языка
    change_language = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_lang_label"]')
    change_language.click()
    sleep(1)

    # Выбираем Индонезийский язык
    indonesia = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="Bahasa Indonesia"]')
    indonesia.click()
    sleep(1)

    # Переходим в настройки
    settings = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="Pengaturan"]')
    settings.click()
    sleep(1)

    # Выбираем смену языка
    change_language = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_lang_label"]')
    change_language.click()
    sleep(1)

    # Выбираем Урду язык
    urdu = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="اردو"]')
    urdu.click()
    sleep(1)

    # Переходим в настройки
    settings = driver.find_element(By.XPATH, '//android.widget.FrameLayout[@content-desc="ترتیبات"]')
    settings.click()
    sleep(1)

    # Выбираем смену языка
    change_language = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_lang_label"]')
    change_language.click()
    sleep(1)

    # Выбираем Хинди язык
    hindi = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="हिन्दी"]')
    hindi.click()
    sleep(1)



