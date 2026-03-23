## 📁 Структура проекта

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
├── conftest.py              # 🔝 Корневой conftest (общие фикстуры). В нем открывается браузер
└── requirements.txt         #     Зависимости (pip install -r requirements.txt)
```

---
