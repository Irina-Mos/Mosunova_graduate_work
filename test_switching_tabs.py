import time
import allure
import pytest
from selenium.webdriver.common.by import By

@allure.id("001")
@allure.feature("Dodo")
@allure.label("Api test")
@allure.title("Переключение между вкладками")
@allure.description("Проверка переключения между основными вкладками меню сайта")
@pytest.mark.dodo_tests

def test_tabs(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        driver.get("https://dodopizza.ru/perm")
    with allure.step('Проверка переключения между вкладками.'):
        tabs = driver.find_elements(By.XPATH, "//a[@class='sc-1c0ft0g-0 gHYwAJ sc-1uavg9b-7 comGOc']")
        for tab in tabs:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
            text = tab.text
            tab.click()
            title = driver.find_element(By.XPATH, f"//h2[text()='{text}']")
            assert text == title.text
            print(tab.text)
            time.sleep(3)

