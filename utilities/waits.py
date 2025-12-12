from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

DEFAULT_TIMEOUT = 10


class Waits:

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator):
        """
        Wait for element to be visible on UI
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Element {locator} not visible after {self.timeout}s")

    def wait_for_element_clickable(self, locator):
        """
        Wait for element to be clickable
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            raise Exception(f"Element {locator} not clickable after {self.timeout}s")

    def wait_for_element_present(self, locator):
        """
        Wait for presence of element in DOM
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(f"Element {locator} not present after {self.timeout}s")

    def wait_for_page_load(self):
        """
        Wait until document.readyState == 'complete'
        """
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
