from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    """
    Klasa bazowa, z ktorej będą korzystały wszystkie strony (pages)
    """

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()
        self.alert = Alert(self.driver)
        self.wait = WebDriverWait(self.driver, 2)

    def _verify_page(self):
        """Autotest strony - uruchamiany automatycznie po wejściu w nią"""
        return

