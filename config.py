# config.py

from appium.options.android import UiAutomator2Options

# Настройки для телефона Motorola
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='ZY32FX9296',  # Phone Motorola
    platformVersion='11',
    appPackage='com.tradingcourses.learnhowtoinvest',
    appActivity='com.trade.test.ui.splash.SplashActivity',
    language='en',
    locale='US',
)

# Опции для драйвера
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

# URL Appium сервера
appium_server_url = 'http://localhost:4723'
