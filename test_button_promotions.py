import allure
import pytest
from selenium.webdriver.common.by import By

@allure.id("004")
@allure.feature("Dodo")
@allure.label("Api test")
@allure.title('Проверка работы кнопки "Акции"')
@allure.description("Проверка открытия страницы с акциями")
@pytest.mark.dodo_tests


def test_promotions(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        driver.get("https://dodopizza.ru/perm")
    with allure.step('Проверка работы кнопки "Акции".'):
        promotions = driver.find_element(By.XPATH, "//a[@class='sc-1c0ft0g-0 gHYwAJ sc-1uavg9b-6 bqLRwB']")
        promotions.click()
    with allure.step('Проверяем, что открылась страница с акциями.'):
        assert "bonusactions" in driver.current_url, "Переход на страницу с акциями."

