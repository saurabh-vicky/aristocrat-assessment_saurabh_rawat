from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.app_logo = (By.CLASS_NAME, "app_logo")
        self.product_name = (By.XPATH, "//a[contains(@id, '_title_link')]")
        self.product_price = (By.XPATH, "//div[@data-test='inventory-item-price']")
        self.burger_button = (By.ID, "react-burger-menu-btn")
        self.log_out_button = (By.ID, "logout_sidebar_link")

    def get_logo_text(self):
        return self.wait.wait_for_element_present(self.app_logo).text

    def log_out(self):
        self.wait.wait_for_element_clickable(self.burger_button).click()
        self.wait.wait_for_element_clickable(self.log_out_button).click()

    def product_details(self):
        self.wait.wait_for_page_load()
        product_name = [product.text for product in self.driver.find_elements(*self.product_name)]
        product_price = [product.text for product in self.driver.find_elements(*self.product_price)]
        return product_name, product_price
