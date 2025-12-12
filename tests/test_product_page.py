from pages.login import LoginPage
from pages.product import ProductPage
from utilities.product import save_data
from utilities.waits import Waits


def test_product_inspection(browser, standard_user_data, login_url):
    username, password = standard_user_data
    wait = Waits(browser)
    login = LoginPage(browser, wait)
    login.get(login_url)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()
    product = ProductPage(browser, wait)
    name, price = product.product_details()
    save_data(name, price)
    product.log_out()
    assert "Swag Labs" == login.get_logo_text()

