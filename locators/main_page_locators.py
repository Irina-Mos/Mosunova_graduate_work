from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = "https://dodopizza.ru/perm"
    MAIN_TABS = (By.XPATH, "//a[@class='sc-1c0ft0g-0 gHYwAJ sc-1uavg9b-7 comGOc']")
    PROMOTIONS = (By.XPATH, "//a[@class='sc-1c0ft0g-0 gHYwAJ sc-1uavg9b-6 bqLRwB']")
    DODOCOINS = (By.XPATH, "//a[@href='/perm/loyaltyprogram']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='sc-18x94tv-0 bHRGrp']")
    LOGIN_MODAL = (By.XPATH, "//div[@class='sc-1ne9bn6-0 cBbDbs sc-17puf9f-0 kWAHdh']")
    PHONE_FIELD = (By.XPATH,"//div[@class='sc-8yov1q-0 rExVf']")
    SHOPPING_CART = (By.XPATH, "//button[@class='sc-18x94tv-0 bHRGrp sc-1uavg9b-11 kFoTqd']")
    SHOPPING_CART_MODAL = (By.XPATH, "//main[@class='sc-1gxjiqu-0 gbQRcz']")
    SHOPPING_CART_FIELD = (By.XPATH,"//button[@class='button-close']")
    LIVE_BROADCAST_BUTTON = (By.XPATH, "//a[@class = 'sc-1c0ft0g-0 gHYwAJ sc-1h8wv3w-4 eTBdfT']")
    LIVE_BROADCAST = (By.XPATH, "//div[@class = 'sc-kfrsub-0 SlrKw']")
    WORK_IN_DODO = (By.XPATH, "//a[@href = 'https://rabotavdodo.ru/?utm_source=web']")
    ABOUT_US = (By.XPATH, "//a[@href = '/perm/about']")
    CONTACTS = (By.XPATH, "//a[@href = '/perm/contacts']")
    CORPORATE_ORDERS = (By.XPATH, "//a[text ()= 'Корпоративные заказы']")
    CORPORATE_ORDERS_MODAL = (By.CSS_SELECTOR, ".popup-container")
    SERTIFICATES_FOR_BUSINESS = (By.XPATH, "//a[text ()= 'Сертификаты для бизнеса']")