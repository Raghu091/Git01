import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObject.Loginpage import Loginpage


@pytest.mark.usefixtures("setup")
class Testlogin:
    def test_Homepage(self):
        login=Loginpage(self.driver)
        login.enterusername().send_keys("Admin")
        login.enterpassword().send_keys("admin123")
