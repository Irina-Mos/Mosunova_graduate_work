from selenium.webdriver.common.by import By


class MainPageLocators:
    URL = "https://dodopizza.ru/perm"
    MAIN_TABS = (By.XPATH, "//a[@class='sc-1c0ft0g-0 gHYwAJ sc-1uavg9b-7 comGOc']")
    PROMOTIONS = (By.XPATH, "//a[@class='sc-1c0ft0g-0 gHYwAJ sc-1uavg9b-6 bqLRwB']")
    DODOCOINS = (By.XPATH, "//a[@href='/perm/loyaltyprogram']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='sc-18x94tv-0 hNSEqk']")
    LOGIN_MODAL = (By.XPATH, "//div[@class='sc-1ne9bn6-0 eOsDZW sc-17puf9f-0 bWXvcs']")
    PHONE_FIELD = (By.XPATH,"//div[@class='sc-8yov1q-0 gFACJZ']")
    SHOPPING_CART = (By.XPATH, "//button[@class='sc-18x94tv-0 hNSEqk sc-1uavg9b-11 eETFSt']")
    SHOPPING_CART_MODAL = (By.XPATH, "//main[@class='sc-1gxjiqu-0 dqtuND']")
    SHOPPING_CART_FIELD = (By.XPATH,"//button[@class='button-close']")
    LIVE_BROADCAST_BUTTON = (By.XPATH, "//a[@class = 'sc-1c0ft0g-0 gHYwAJ sc-1h8wv3w-4 hnsJbe']")
    LIVE_BROADCAST = (By.XPATH, "//div[@class = 'sc-kfrsub-0 dWySFT']")