from pages.rostelekom import MainPage

"""АВТОРИЗАЦИЯ... ТЕСТЫ."""
"""Авторизация с корректной учетной записью. ТЕСТ 17."""
def test_authorization_valid_data(web_browser):
    page = MainPage(web_browser)
    page.link_enter_email.click()
    page.search_email_authorization = 'rudenkov.sereja@yandex.ru'
    page.search_password_authorization = '12345VFvf'
    page.button_enter_authorization.click()
    assert page.name_user.get_text() == "Петров\nАлексей"

"""Авторизация с пустым полем 'email'. ТЕСТ 18."""
def test_authorization_empty_email(web_browser):
    page = MainPage(web_browser)
    page.link_enter_email.click()
    page.search_email_authorization = ''
    page.search_password_authorization = '12345VFvf'
    page.button_enter_authorization.click()
    assert page.error_red_text_email_authorization.get_text() == 'Введите адрес, указанный при регистрации'

"""Авторизация с пустым полем 'пароль'. ТЕСТ 19. БАГ."""
"""После нажатия на кнопку 'войти', действий не происходит. БАГ-5."""
def test_authorization_empty_password(web_browser):
    page = MainPage(web_browser)
    page.link_enter_email.click()
    page.search_email_authorization = 'oleg.kovr@mail.ru'
    page.search_password_authorization = ''
    page.button_enter_authorization.click()

"""Авторизация с пробелом в пароле. ТЕСТ 20."""
def test_authorization_whitespace_password(web_browser):
    page = MainPage(web_browser)
    page.link_enter_email.click()
    page.search_email_authorization = 'oleg.kovr@mail.ru'
    page.search_password_authorization = '12345 VFvf'
    page.button_enter_authorization.click()
    assert page.invalid_login_or_password.get_text() == 'Неверный логин или пароль'

"""Авторизация с пустым полем 'телефон'. ТЕСТ 21."""
def test_authorization_empty_phone(web_browser):
    page = MainPage(web_browser)
    page.link_enter_phone.click()
    page.search_phone_authorization = ''
    page.search_password_authorization = '12345VFvf'
    page.button_enter_authorization.click()
    assert page.error_red_text_phone_authorization.get_text() == 'Введите номер телефона'

