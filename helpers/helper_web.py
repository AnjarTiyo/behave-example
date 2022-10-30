from selenium import webdriver

from helpers.helper_base import HelperFunc


def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome())
    if browser == "firefox":
        return HelperFunc(webdriver.Firefox())
    else:
        return HelperFunc(webdriver.Firefox())
