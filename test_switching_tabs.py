import time
import allure
import pytest
from selenium.webdriver.common.by import By


def test_tabs(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        driver.get("https://dodopizza.ru/perm")
    with allure.step('Проверка переключения между вкладками.'):
        tabs = driver.find_elements(By.XPATH, "//a[@class='sc-1c0ft0g-0 gHYwAJ sc-1uavg9b-7 comGOc']")
        for tab in tabs:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
            tab.click()
            print(tab.text)
            time.sleep(3)

