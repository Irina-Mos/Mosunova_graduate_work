import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_tabs():
    driver = webdriver.Chrome()
    with allure.step('Открываем сайт "ДоДо".'):
        driver.get("https://dodopizza.ru/perm")
    with allure.step('Проверка переключения между вкладками.'):
        tabs = driver.find_elements(By.XPATH, "//a[@class='sc-1c0ft0g-0 gHYwAJ sc-1uavg9b-7 comGOc']")
        for tab in tabs:
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tab)
            location_before = title.location()
            tab.click()
            title = driver.find_element(By.XPATH, "//h2[text()='Пиццы']")
            location_after = title.location()
            assert location_before != location_after
            print(tab.text)
            time.sleep(3)

