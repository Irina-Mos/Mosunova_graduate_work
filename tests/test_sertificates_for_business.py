import allure
import pytest
from pages.page_main import MainPage

@allure.id("011")
@allure.label("Dodo")
@allure.title('Проверка работы кнопки "Сертификаты для бизнеса" в шапке сайта')
@allure.description("Проверка открытия страницы с сертификатвми для бизнеса.")
@pytest.mark.dodo_tests

def test_sert_for_business(driver):
    with allure.step('Открываем сайт "ДоДо".'):
        web = MainPage(driver)
        web.open()

    with allure.step('Нажимаем на кнопку "Сертификаты для бизнеса".'):
        web.select_sertifies_for_business()

    with allure.step('Проверяем, что открылась страница с сертификатами для бизнеса.'):
        assert "certificates" in driver.current_url, "Переход на страницу с сертификатами для бизнеса не произошел."