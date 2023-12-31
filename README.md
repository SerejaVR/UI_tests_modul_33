## Введение.
Репозиторий содержит пример использования шаблона PageObject с Selenium и Pytest.
### В нем находится:
  * __папка "pages":__
    * __файл <base.py>__ - содержит реализацию шаблона PageObject для Python.
    * __файл <elements.py>__ - содержит вспомогательный класс для определения веб-элементов на веб-страницах.
    * __файл <rostelekom.py>__ - содержит базовый функционал, для тестовых сценариев регистрации и авторизации на сайте "Ростелеком".
  * __файл <conftest.py>__ - содержит набор фикстур используемых в Pytest.
  * __файл <requirements.py>__ - содержит список инструментов-библиотек, котрые необходимо установить для запуска тестов:
    * __pytest 6.2.5__ - среда тестирования Python, для написания и выполнения тестового кода.
    * __selenium 4.9.0__ - библиотека используемая для управления различными браузерами.
    * __pytest-selenium 4.0.0__ - фреймворк для написания, запуска тестов и взаимодействия с веб-элементами.
    * __termcolor 2.3.0__ - библиотека отвечающая за цвет и фон.
    * __allure-python-commons 2.13.2__ - общий движок для всех модулей, полезно для интеграции с самодельными фреймворками.
  * __папка "tests":__
    * __файл <test_rtk_registration.py>__ - содержит несколько авто-тестов дымового веб-интерфейса для сайта "Ростелеком", функционала регистрации.
    * __файл <test_rtk_authorization.py>__ - содержит несколько авто-тестов дымового веб-интерфейса для сайта "Ростелеком", функционала авторизации.

    '''Тест-кейсы оформлены в виде отдельных функций, для их создания были применены техники тест-дизайна:
    * методы основанные на опыте:
      * исследовательское тестирование - проверка системы с позиции пользователя.
      * предположение об ошибках - поиск  наиболее вероятных типов дефектов и дефектов найденных в схожих проектах, используя опыт.
    * методы основанные на спецификации:
      * эквивалентное разбиение на классы - ввод параметров разных классов при составлении тест-кейсов.
      * анализ граничных значений - проверка поведения системы, при вводе данных граничащих с допустимым диапазоном.
      * таблицы принятия решений - осуществление визуального контроля, при составлении тестовых сценариев.'''
## Запуск авто-тестов.
1. Установите все требования указанные в файле \<requirements>.
2. Загрузите Selenium WebDriver. [ссылка для загрузки WebDriver](https://chromedriver.chromium.org/downloads) , выберите версию совместимую с вашим браузером.
3. Команда для запуска тестов:
   python -m pytest -v --driver Chrome --driver-path <путь к драйверу>.exe tests\\<файл с тестами>.py
   
