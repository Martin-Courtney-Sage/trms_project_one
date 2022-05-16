# SELENIUM SHOWCASE

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.site_home import SiteHomePage

serv = Service("C:/Users/Mysti/Desktop/Revature/ChromeDriver/chromedriver.exe")
driver: WebDriver = webdriver.Chrome(service=serv)
site_home = SiteHomePage(driver)


def test_nav(lang_func, title):
    sleep(1.2)
    lang_func().click()
    sleep(2.5)
    assert title == driver.title


def _test():
    nav_test1 = [(site_home.login, "Login")]
    nav_test2 = [(site_home.about, "About/Contact")]
    nav_test3 = [(site_home.home, "Main Home Page")]

    for func, title in nav_test1:
        driver.get("file:///C:/Users/Mysti/Desktop/Revature/VisualStudioThings/ClientSideTechnologies/TRMS%20Project/HTML/homepage.html")
        try:
            test_nav(func, title)
        except AssertionError as e:
            print(f"Test: {func.__name__} - Failed\n Expected: {title}\n Actual: {driver.title}")
        else:
            print(f"Test: {func.__name__} - Passed")
        break

    for func, title in nav_test2:
        try:
            test_nav(func, title)
        except AssertionError as e:
            print(f"Test: {func.__name__} - Failed\n Expected: {title}\n Actual: {driver.title}")
        else:
            print(f"Test: {func.__name__} - Passed")
        break

    for func, title in nav_test3:
        try:
            test_nav(func, title)
        except AssertionError as e:
            print(f"Test: {func.__name__} - Failed\n Expected: {title}\n Actual: {driver.title}")
        else:
            print(f"Test: {func.__name__} - Passed")
        break

    driver.quit()


if __name__ == '__main__':
    _test()
