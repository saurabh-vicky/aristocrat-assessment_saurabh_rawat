from pages.login import LoginPage
from pages.product import ProductPage
from utilities.waits import Waits


def test_standard_user_login(browser, standard_user_data, login_url):
    username,password = standard_user_data
    wait = Waits(browser)
    login = LoginPage(browser, wait)
    login.get(login_url)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()
    product = ProductPage(browser, wait)
    assert product.get_logo_text() == "Swag Labs"


def test_locked_user_login(browser, locked_user_data, login_url):
    username, password = locked_user_data
    wait = Waits(browser)
    login = LoginPage(browser, wait)
    login.get(login_url)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()
    assert "Sorry, this user has been locked out" in login.locked_user_message()