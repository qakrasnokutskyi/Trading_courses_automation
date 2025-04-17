# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
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
        android_driver.quit()

# -------------------------------------------------------------------------------
# --- Utils ---
# -------------------------------------------------------------------------------

def rotate_screen(driver, orientation):
    # orientation: 'LANDSCAPE' or 'PORTRAIT'
    driver.orientation = orientation

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_choose_middle_after_onboard(driver):
    sleep(7)

    # Выбираем англ язык
    english = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.tradingcourses.learnhowtoinvest:id/tv_name" and @text="English"]')
    english.click()
    sleep(1)

    # Выполнение свайпа влево между разделами онбоард страницы
    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.8  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.2  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.8  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.2  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.8  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.2  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.2  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.8  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

# Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.2  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.8  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    # Получаем координаты элементов для свайпа
    element = driver.find_element(By.XPATH,
                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout')
    size = driver.get_window_size()

    # Начальные и конечные координаты для свайпа влево
    start_x = size['width'] * 0.2  # Начальная точка (80% от ширины экрана)
    end_x = size['width'] * 0.8  # Конечная точка (20% от ширины экрана)
    start_y = size['height'] / 2  # Центр экрана по высоте

    # Свайп с использованием метода swipe() (если используется более старая версия Appium)
    driver.swipe(start_x, start_y, end_x, start_y, 1000)  # Время свайпа - 1000 миллисекунд
    sleep(1)

    #Нажимаем кнопку "BEGIN TRAINING"
    start_button = driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button')
    start_button.click()
    sleep(5)

    #Выбираем "Средний курс"
    intermediate = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]')
    intermediate.click()
    sleep(5)

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------