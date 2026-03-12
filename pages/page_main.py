from  pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
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

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def check_tabs(self):
        tabs = self.driver.find_elements(self.MAIN_TABS)
        for tab in tabs:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
            text = tab.text
            tab.click()
            title = self.driver.find_element(By.XPATH, f"//h2[text()='{text}']")
            assert text == title.text
            time.sleep(3)

    def select_promotions(self):
        self.click(self.PROMOTIONS)

    def select_dodocoins(self):
        self.click(self.DODOCOINS)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        time.sleep(3)

    def wait_login_modal(self):
        return self.wait_element(self.LOGIN_MODAL)

    def wait_phone_field(self):
        return self.wait_element(self.PHONE_FIELD)
