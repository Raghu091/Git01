import time

import pytest
from selenium import  webdriver


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\raghunath.chandrasek\\Downloads\\New folder\\chromedriver.exe")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    time.sleep(10)
    yield
    driver.close()
