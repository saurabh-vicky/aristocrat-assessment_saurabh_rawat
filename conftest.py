import pytest
# import to load data from .ini file
import os
import configparser
# Imports to get chrome driver working
from selenium import webdriver


config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'pytest.ini')
config.read(config_path)


@pytest.fixture(scope="session")
def standard_user_data():
    username = config.get('STANDARD_USER', 'username')
    password = config.get('STANDARD_USER', 'password')
    return username, password


@pytest.fixture(scope="session")
def locked_user_data():
    username = config.get('LOCKED_OUT_USER', 'username')
    password = config.get('LOCKED_OUT_USER', 'password')
    return username, password


@pytest.fixture(scope="session")
def login_url(request):
    return config.get('URL', 'base_url')


@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    })
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()