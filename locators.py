# locators.py

from appium.webdriver.common.appiumby import AppiumBy

# -------------------------------------------------------------------------------
# --- Selectors ---
# -------------------------------------------------------------------------------

class Languages:
    ENGLISH = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')
    RUSSIAN = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Русский")')
    UKRAINE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Українська")')
    DEUTSCH = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Deutsch")')
    INDONESIA = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Bahasa Indonesia")')
    URDU = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("اردو")')
    HINDI = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("हिन्दी")')

class Login:
    BTN_REGISTRATION_LOGIN = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_enter")')
    FIELD_EMAIL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Your email")')
    FIELD_PASSWORD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Your password")')
    BTN_SUBMIT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses:id/submit_btn")')
    BTN_SIGNIN = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_signIn")')
    PAGE_REGISTRATION = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_tab_reg")')
    PAGE_LOGIN = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_tab_auth")')
    FIELD_NAME = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Your name")')

    LOGO_APPLICATION = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_title")')

class Navigation:
    TRAINING = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/studying")')
    TRADING = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Trading")')
    BROKERS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Brokers")')
    SETTINGS = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings")')

class MainPage:
    DEMO_BALANCE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_balance_label")')
    CHANGE_COURSE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_change_course")')

class TradingPage:
    CURRENCY_PAIR = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_cur_arrow")')
    TIMEFRAME = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_timeframe")')
    SWITCH_GRAPHIC = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_switch")')
    INDICATORS = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_indicators")')
    DEMO_BALANCE_TRADING = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_balance")')


    BTN_VIDEO = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_add_coins")')
    BTN_WATCH = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_watch")')
    BTN_CLOSE_VIDEO = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/close")')
    BTN_LIVE_ACCOUNT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_real_balance")')
    BTN_HISTORY_TRADE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_history")')

    BUY = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/cl_buy")')
    SELL = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/cl_sell")')

class CurrencyPairs:
    AUD_USD = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("AUD/USD")')
    BTC_USD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("BTC/USD")')
    CHF_USD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CHF/USD")')
    EUR_USD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("EUR/USD")')
    JPY_USD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("JPY/USD")')
    NZD_USD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NZD/USD")')
    RUB_USD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("RUB/USD")')

class Indicators:
    INDICATOR_MOVING = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Moving Average")')
    INDICATOR_MOMENTUM = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Momentum")')
    MOVING_SMA = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_sma")')
    MOVING_EMA = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_ema")')
    MOVING_SMMA = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_smma")')
    BTN_ACCEPT_INDICATOR = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_accept")')
    COLOR = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/ll_color_picked")')
    DELETE_INDICATOR = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_remove")')
    PAGE_ACTIVE_INDICATORS = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_active")')
    EDIT_INDICATOR = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_setting")')
    WIDTH = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/imageView5")')

class IndicatorColors:
    BLUE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/fl3")')
    RED = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/fl1")')
    GREEN = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/fl2")')
    WHITE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/fl4")')

class IndicatorsWidth:
    WIDTH_1 = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/fl_w1")')
    WIDTH_2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/fl_w2")')
    WIDTH_3 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/fl_w3")')
    WIDTH_4 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/fl_w4")')
    WIDTH_5 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/fl_w5")')

class TimeFrame:
    TIMEFRAME_S20 = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_s20")')
    TIMEFRAME_M1 = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_m1")')
    TIMEFRAME_M2 = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_m2")')

class HistoryTrade:
    BTN_BACK = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/iv_back")')

class BrokerPage:
    BTN_NEXT_POCKET_OPTION = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_go_over").instance(0)')

    TITLE_BROKERS = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Top brokers")')
    MIN_DEPOSIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_next_title").instance(0)')
    RATING = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_title12").instance(0)')
    BTN_NEXT_BROKER = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/bt_go_over").instance(0)')
    DATE_BROKERS = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_date_title")')

class Course:
    BEGINNER_COURSE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/ll_beginner")')
    MIDDLE_COURSE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/ll_middle")')
    PRO_COURSE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/ll_pro")')
    ADVANCED_COURSE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/ll_pro_plus")')

class SettingsPage:
    SETTINGS_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_next_title")')
    USER_EMAIL = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_email_label")')
    CHANGE_LANGUAGE = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.tradingcourses.learnhowtoinvest:id/tv_lang_label")')
    SEND_FEEDBACK = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Send Feedback")')
    RATE_US = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Please rate us")')
    QUIT = (AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Quit")')

