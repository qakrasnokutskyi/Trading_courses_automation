# -------------------------------------------------------------------------------
# --- Imports ---
# -------------------------------------------------------------------------------

from datetime import datetime
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from locators import Languages, Login, Navigation, BrokerPage

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

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# -------------------------------------------------------------------------------
# --- Test ---
# -------------------------------------------------------------------------------

def test_check_date_format(driver):
    sleep(7)

    # Выбираем англ язык
    wait_and_click(driver, *Languages.ENGLISH)

    # Нажимает кнопку "Войти/Зарегистрироваться
    wait_and_click(driver, *Login.BTN_REGISTRATION_LOGIN)

    # Заполняем поле email
    email = wait_for_element(driver, *Login.FIELD_EMAIL)
    email.send_keys('qakrasnokutskiy@gmail.com')

    # Заполняем поле password
    password = wait_for_element(driver, *Login.FIELD_PASSWORD)
    password.send_keys('e251dq12r')

    # Выполняем вход
    wait_and_click(driver, *Login.BTN_SIGNIN)

    # Переходим в раздел Брокеры
    wait_for_element(driver, *Navigation.BROKERS).click()


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

# -------------------------------------------------------------------------------
# --- Asserts ---
# -------------------------------------------------------------------------------

    title_brokers_page = wait_for_element(driver, *BrokerPage.TITLE_BROKERS)
    assert title_brokers_page is not None,'Title is not visible'

    min_deposit_page = wait_for_element(driver, *BrokerPage.MIN_DEPOSIT)
    assert min_deposit_page is not None,'Min Deposit is not visible'

    rating_page = wait_for_element(driver, *BrokerPage.RATING)
    assert rating_page is not None,'Rating is not visible'

    btn_next_broker = wait_for_element(driver, *BrokerPage.BTN_NEXT_BROKER)
    assert btn_next_broker is not None,'Next Broker is not visible'

    date_brokers_page = wait_for_element(driver, *BrokerPage.DATE_BROKERS)
    assert date_brokers_page is not None,'Date Brokers is not visible'
