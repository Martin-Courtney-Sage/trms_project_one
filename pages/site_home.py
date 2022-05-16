# SELENIUM SET-UP

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class SiteHomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def home(self):
        return self.driver.find_element(by=By.ID, value="home-link")

    def login(self):
        return self.driver.find_element(by=By.ID, value="login-link")

    def about(self):
        return self.driver.find_element(by=By.ID, value="about-contact-link")


