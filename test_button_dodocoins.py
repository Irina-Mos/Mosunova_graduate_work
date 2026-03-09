import allure
import pytest
from selenium.webdriver.common.by import By

@allure.id("002")
@allure.feature("Dodo")
@allure.label("Api test")
@allure.title('Проверка работы кнопки "Додокоины"')
@allure.description("Проверка открытия страницы с программой лояльности")
@pytest.mark.dodo_tests


def test_dodocoins(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        driver.get("https://dodopizza.ru/perm")
    with allure.step('Проверка работы кнопки "Додокоины".'):
        dodocoins = driver.find_element(By.XPATH, "//a[@href='/perm/loyaltyprogram']")
        dodocoins.click()
    with allure.step('Проверяем, что открылась страница программы лояльности.'):
        assert "loyaltyprogram" in driver.current_url, "Переход на страницу лояльности не произошёл."

