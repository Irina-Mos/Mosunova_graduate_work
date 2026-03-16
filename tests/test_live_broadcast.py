import allure
import pytest
from pages.page_main import MainPage

from selenium import webdriver

driver = webdriver.Chrome()
fr = driver

@allure.id("006")
@allure.label("Dodo")
@allure.title("Проверка кнопок в шапке сайта")
@allure.description("Проверка перехода по соответствующим ссылкам при нажатии кнопок в шапке сайта")
@pytest.mark.dodo_tests

def test_tabs(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()

    with allure.step('Проверка работы кнопки "Прямой эфир".'):
        web.click_live_broadcast_button()
        assert web.wait_live_broadcast(), "Прямой эфир не отображается"
