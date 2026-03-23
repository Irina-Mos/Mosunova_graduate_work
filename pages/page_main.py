from  pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
import time


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def open(self):
        self.driver.get(self.locators.URL)
        return self

    def check_tabs(self):
        tabs = self.wait_elements(self.locators.MAIN_TABS)
        for tab in tabs:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
            text = tab.text
            tab.click()
            title = self.driver.find_element(By.XPATH, f"//h2[text()='{text}']")
            assert text == title.text
            time.sleep(3)

    def select_promotions(self):
        self.click(self.locators.PROMOTIONS)

    def select_dodocoins(self):
        self.click(self.locators.DODOCOINS)

    def click_login(self):
        self.click(self.locators.LOGIN_BUTTON)
        time.sleep(3)

    def wait_login_modal(self):
        return self.wait_element(self.locators.LOGIN_MODAL)

    def wait_phone_field(self):
        return self.wait_element(self.locators.PHONE_FIELD)

    def click_shp_cart(self):
        self.click(self.locators.SHOPPING_CART)
        time.sleep(3)

    def wait_shp_cart_modal(self):
        return self.wait_element(self.locators.SHOPPING_CART_MODAL)

    def wait_shp_cart_field(self):
        return self.wait_element(self.locators.SHOPPING_CART_FIELD)

    def click_live_broadcast_button(self):
        self.click(self.locators.LIVE_BROADCAST_BUTTON)
        time.sleep(3)

    def wait_live_broadcast(self):
        return self.wait_element(self.locators.LIVE_BROADCAST)

    def select_work_in_dodo(self):
        self.click(self.locators.WORK_IN_DODO)

    def select_about_us(self):
        self.click(self.locators.ABOUT_US)

    def select_contacts(self):
        self.click(self.locators.CONTACTS)

    def select_corporate_orders(self):
        self.click(self.locators.CORPORATE_ORDERS)

    def wait_corporate_order_modal(self):
        return self.wait_element(self.locators.CORPORATE_ORDERS_MODAL)

    def select_sertificates_for_business(self):
        self.click(self.locators.SERTIFICATES_FOR_BUSINESS)


