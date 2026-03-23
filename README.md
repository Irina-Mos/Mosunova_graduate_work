## О чем проект?

```
Проект в автоматизированными тестами главной страницы сайта "Додо пицца" (https://dodopizza.ru/perm).

```

## Начало работы
```
Перед началом работы установить requirements.txt. Ввести команду в терминале: pip install -r requirements.txt.

```
## Запуск автоматизированных тестов

```
Для запуска автоматизированных тестов использовать команду в терминале: pytest -m dodo_tests.

``` 

## Структура проекта

```
dodo_project/
│
├──allure_results/                          #  Allure-Отчет(allure serve allure_results)
│
│
├──checklist_and_test_cases                 #  Чек-лист и тест-кейсы
│
│
├──locators                                 # Переменные (локаторы)
│
│
├── pages/                   
│   ├── base_page.py                        #     Базовый класс (общие методы для всех страниц)
│   └── main_page.py                        #     Главная страница
│
├── tests/                                  # ✅ Тесты
│   ├── test_about_us.py                    #     Тест кнопки "О нас"
│   ├── test_button_dodocoins.py            #     Тест кнопки "Додокоины"
│   ├── test_button_login.py                #     Тест кнопки "Войти"
│   ├── test_button_promotions.py           #     Тест кнопки "Акции"
│   ├── test_button_shopping_cart.py        #     Тест кнопки "Корзина"
│   ├── test_contacts.py                    #     Тест кнопки "Контакты"
│   ├── test_corporation_order.py           #     Тест кнопки "Корпоративные заказы"
│   ├── test_live_broadcast.py              #     Тест кнопки "Прямой эфир"
│   ├── test_sertificates_for_business.py   #     Тест кнопки "Сертификаты для бизнеса"
│   ├── test_switching_tabs.py              #     Тест переключение между вкладками меню 
│   └── test_work_in_dodo.py                #     Тест кнопки "Работа в Додо"
│
│
├── conftest.py                             #    Корневой conftest (общие фикстуры). В нем открывается браузер
└── requirements.txt                        #    Зависимости (pip install -r requirements.txt)
```

## Пример автоматизированного теста (test_button_shopping_cart.py):
```python
# Импорт библиотек
import allure        
import pytest
from pages.page_main import MainPage
# Декораторы Allure и Pytest
@allure.id("005")       # Присвоение тесту уникального идентификатора
@allure.label("Dodo")       # Добавление тесту метки
@allure.title('Проверка работы кнопки "Корзина"')       # Название теста
@allure.description("Проверка открытия модального окна с корзиной заказа")      # Описание теста
@pytest.mark.dodo_tests     # Присвоение метки для запуска группы тестов с этой меткой (команда pytest -m dodo_tests)
# Объявление функции теста
def test_shopping_cart(driver):
    with allure.step('Открываем сайт "ДоДо".'):     # Начинает блок шага в отчете Allure
        web = MainPage(driver)      # Создание объекта класса MainPage
        web.open()      # Открытие браузера и переход на адрес сайта
    with allure.step('Нажимаем на кнопку "Корзина".'):     # Начинает новый шаг в отчете Allure
        web.click_shp_cart()        # Вызов метода клика по кнопке корзины        
        assert web.wait_shp_cart_modal(), "Модальное окно не открылось."        # Проверка открытия корзины 


    with allure.step('Проверяем, что открылось модальное окно с корзиной заказа.'):     # Начинает третий шаг в отчете Allure
        assert web.wait_shp_cart_field(),"Поле c корзиной заказа не найдено."       # Вторая проверка. Поиск поля внутри корзины

    web.take_screenshot("Модальное окно корзины заказа.")       # Вызов метода создания скриншота
# После прохождения тестов для отображения результатов создать Allure - отчет: команда в терминале "allure serve allure_results" 
```

