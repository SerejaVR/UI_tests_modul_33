import os
from pages.base import WebPage
from pages.elements import WebElement
import time


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            # time.sleep(5)
            url = os.getenv("MAIN_URL") or 'https://b2c.passport.rt.ru/'
        super().__init__(web_driver, url)

                                # РЕГИСТРАЦИЯ.
# ссылка зарегестрирваться
    button_reg = WebElement(xpath='//*[@id="kc-register"]')
# поле имя
    search_name = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]')
# поле фамилия
    search_surname = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]')
# поле почта или телефон
    search_email = WebElement(xpath='//*[@id="address"]')
# поле пароль
    search_password = WebElement(xpath='//*[@id="password"]')
# поле подтверждение пароля
    search_password_confirm = WebElement(xpath='//*[@id="password-confirm"]')
# кнопка зарегестрироваться
    button_reg_email_pass = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]')
# заголовок "Подтверждение email"
    title_email = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/h1[1]')
# текст ошибки при некорректном вводе имени
    error_red_text_name = WebElement(xpath='//span[text()="Необходимо заполнить поле кириллицей. От 2 до 30 символов."]')
# текст ошибки при некорректном вводе фамилии
    error_red_text_surname = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')
# текст ошибки при некорректном вводе 'email' или 'телефона'
    error_red_text_email_phone = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/span[1]')
# текст ошибки при некорректном вводе пароля
    error_red_text_password = WebElement(xpath='//span[text()="Пароль должен содержать только латинские буквы"]')
# текст ошибки при вводе меньше 8-ми символов пароля
    error_red_text_less_symbols_password = WebElement(xpath='//span[text()="Длина пароля должна быть не менее 8 символов"]')
# текст ошибки при вводе больше 20-ти символов пароля
    error_red_text_more_symbols_password = WebElement(xpath='//span[text()="Длина пароля должна быть не более 20 символов"]')
# текст ошибки при вводе пароля в вехнем регистре
    error_red_text_big_letters_password = WebElement(xpath='//span[text()="Пароль должен содержать хотя бы одну строчную букву"]')
# текст ошибки при вводе пароля в нижнем регистре
    error_red_text_small_letters_password = WebElement(xpath='//span[text()="Пароль должен содержать хотя бы одну заглавную букву"]')
# текст ошибки при несовпадении символов поля "пароль" и поля "подтверждение пароля"
    error_red_text_confirmation_password = WebElement(xpath='//span[text()="Пароли не совпадают"]')

                            # АВТОРИЗАЦИЯ.
# ссылка для ввода почты, при авторизации
    link_enter_email = WebElement(xpath='//*[@id="t-btn-tab-mail"]')
# поле почта, авторизации
    search_email_authorization = WebElement(xpath='//*[@id="username"]')
# поле пароль авторизации
    search_password_authorization = WebElement(xpath='//*[@id="password"]')
# кнопка войти, авторизации
    button_enter_authorization = WebElement(xpath='//*[@id="kc-login"]')
# имя пользователя
    name_user = WebElement(xpath='//*[@id="app"]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]')
# текст ошибки при вводе email, для авторизации
    error_red_text_email_authorization = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')
# текст ошибки, неверный логин или пароль
    invalid_login_or_password = WebElement(xpath='//*[@id="form-error-message"]')
# ссылка для ввода телефона, при авторизации
    link_enter_phone = WebElement(xpath='//*[@id="t-btn-tab-phone"]')
# поле телефон, авторизации
    search_phone_authorization = WebElement(xpath='//*[@id="username"]')
# текст ошибки при вводе телефона, для авторизации
    error_red_text_phone_authorization = WebElement(xpath='//span[text()="Введите номер телефона"]')















