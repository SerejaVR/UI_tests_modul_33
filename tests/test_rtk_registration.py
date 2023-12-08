from pages.rostelekom import MainPage

"""РЕГИСТРАЦИЯ...ТЕСТЫ."""
"""Ввод валидных данных при регистрации. ТЕСТ 1."""
def test_registration_valid(web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr@mail.ru'
    page.search_password = '12345VFvf'
    page.search_password_confirm = '12345VFvf'
    page.button_reg_email_pass.click()
    assert page.title_email.get_text() == "Подтверждение email"

"""Ввод в поле 'имя' латиницы при регистрации. ТЕСТ 2."""
def test_registration_invalid_name(web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Oleg'
    page.search_surname.click()
    assert page.error_red_text_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

"""Ввод в поле 'имя' более 30-ти символов. ТЕСТ 3. БАГ-1."""
"""БАГ.В брифе от заказчика не указано максимальное количество символов для поля 'имя'."""
def test_registration_name_31_simvol(web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Оооооооооолеееееееееггггггггггг'
    page.search_surname.click()
    assert page.error_red_text_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


"""Ввод в поле 'фамилия', 29 символов при регистрации. ТЕСТ 4."""
def test_surname_29_simvol(web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Коооооооооврооооооооввввввввв'
    page.search_email.click()
    assert page.error_red_text_surname.get_text() != "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

"""Ввод в поле 'фамилия', 31 символ при регистрации. ТЕСТ 5. БАГ-2."""
"""БАГ.В брифе от заказчика не указано максимальное количество символов для поля 'фамилия'."""
def test_surname_31_simvol(web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Кооооооооовроооооооовввввввввыы'
    page.search_email.click()
    assert page.error_red_text_surname.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

"""Пустое поле 'email' при регистрации. ТЕСТ 6."""
def test_registration_empty_email (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = ''
    page.search_password = '12345VFvf'
    page.search_password_confirm = '12345VFvf'
    page.button_reg_email_pass.click()
    assert page.error_red_text_email_phone.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

"""Ввод двойного знака @(собака) в поле 'email' при регистрации. ТЕСТ 7."""
def test_registration_double_sign_email (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr@@mail.ru'
    page.search_password = '12345VFvf'
    page.search_password_confirm = '12345VFvf'
    page.button_reg_email_pass.click()
    assert page.error_red_text_email_phone.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

"""Ввод кирриллицы в поле 'email' при регистрации. ТЕСТ 8."""
def test_registration_kirrillica_email (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'олег.ковр@mail.ru'
    page.search_password = '12345VFvf'
    page.search_password_confirm = '12345VFvf'
    page.button_reg_email_pass.click()
    assert page.error_red_text_email_phone.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

"""Ввод пробела в поле 'email' при регистрации. ТЕСТ 9."""
def test_registration_whitespace_email (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr @mail.ru'
    page.search_password = '12345VFvf'
    page.search_password_confirm = '12345VFvf'
    page.button_reg_email_pass.click()
    assert page.error_red_text_email_phone.get_text() == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'

"""Ввод кирриллицы в поле 'пароль' при регистрации. ТЕСТ 10."""
def test_registration_kirrillica_password (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr@mail.ru'
    page.search_password = '12345МАма'
    page.search_password_confirm = '12345МАма'
    page.button_reg_email_pass.click()
    assert page.error_red_text_password.get_text() == 'Пароль должен содержать только латинские буквы'

"""Ввод спецсимволов в поле 'пароль' при регистрации. ТЕСТ 11. БАГ-3."""
"""БАГ. Пароль проходит без единой цифры."""
def test_registration_special_characters_password (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr@mail.ru'
    page.search_password = '!"№;%?VFvf'
    page.search_password_confirm = '!"№;%?VFvf'
    page.button_reg_email_pass.click()
    assert page.title_email.get_text() == "Подтверждение email"

"""Ввод меньше 8-ми символов в поле 'пароль' при регистрации. ТЕСТ 12."""
def test_registration_less_symbols_password (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr@mail.ru'
    page.search_password = '12345Vf'
    page.search_password_confirm = '12345Vf'
    page.button_reg_email_pass.click()
    assert page.error_red_text_less_symbols_password.get_text() == 'Длина пароля должна быть не менее 8 символов'

"""Ввод больше 20-ти символов в поле 'пароль' при регистрации. ТЕСТ 13. БАГ-4."""
"""БАГ.В брифе от заказчика не указано максимальное количество символов для поля 'пароль'."""
def test_registration_more_symbols_password (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr@mail.ru'
    page.search_password = '12345VfVf01234567890!'
    page.search_password_confirm = '12345VfVf01234567890!'
    page.button_reg_email_pass.click()
    assert page.error_red_text_more_symbols_password.get_text() == 'Длина пароля должна быть не более 20 символов'

"""Ввод пароля в вернем регистре при регистрации. ТЕСТ 14."""
def test_registration_big_letters_password (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr@mail.ru'
    page.search_password = '12345VFVF'
    page.search_password_confirm = '12345VFVF'
    page.button_reg_email_pass.click()
    assert page.error_red_text_big_letters_password.get_text() == 'Пароль должен содержать хотя бы одну строчную букву'

"""Ввод пароля в нижнем регистре при регистрации. ТЕСТ 15."""
def test_registration_small_letters_password (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr@mail.ru'
    page.search_password = '12345vfvf'
    page.search_password_confirm = '12345vfvf'
    page.button_reg_email_pass.click()
    assert page.error_red_text_small_letters_password.get_text() == 'Пароль должен содержать хотя бы одну заглавную букву'

"""Ввод в поле 'подтверждение пароля' символов, отличающихся от символов поля 'пароль' при регистрации. ТЕСТ 16."""
def test_registration_confirmation_password (web_browser):
    page = MainPage(web_browser)
    page.button_reg.click()
    page.search_name = 'Олег'
    page.search_surname = 'Ковров'
    page.search_email = 'oleg.kovr@mail.ru'
    page.search_password = '12345VFvf'
    page.search_password_confirm = '12345VFvf12345'
    page.button_reg_email_pass.click()
    assert page.error_red_text_confirmation_password.get_text() == 'Пароли не совпадают'

