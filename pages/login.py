from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.invalid_username_msg = (By.TAG_NAME, "h3")
        self.app_logo = (By.CLASS_NAME, "login_logo")

    def get(self, url):
        #self.wait.wait_for_page_load()
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def get_logo_text(self):
        return self.wait.wait_for_element_present(self.app_logo).text

    def locked_user_message(self):
        return self.driver.find_element(*self.invalid_username_msg).text
