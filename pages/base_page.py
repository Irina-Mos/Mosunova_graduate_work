from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.global_timeout = 10
        self.wait = WebDriverWait(driver, self.global_timeout)

    def wait_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))


    def click(self, locator):
        return self.wait_element(locator).click()

    def take_screenshot(self, text):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=text,
            attachment_type=allure.attachment_type.PNG
        )

    def select_window(self, num_windows=int):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[num_windows])
