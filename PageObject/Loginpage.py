from selenium import webdriver
from selenium.webdriver.common.by import By

class Loginpage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "txtUsername")
    password = (By.NAME, "txtPassword")
    submit = (By.NAME, "Submit")

    def enterusername(self):
        return self.driver.find_element(*Loginpage.username)

    def enterpassword(self):
        return self.driver.find_element(*Loginpage.password)

    def submit(self):
        return self.driver.find_element(*Loginpage.submit)


