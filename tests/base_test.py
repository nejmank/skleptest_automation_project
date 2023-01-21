import unittest
from selenium import webdriver


# from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """Klasa bazowa każdego testu"""

    def setUp(self):
        # Otwarcie przeglądarki
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("http://skleptest.pl/")
        # self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
