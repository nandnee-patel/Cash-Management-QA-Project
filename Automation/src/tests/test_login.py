import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.LoginPage import LoginPage

def test_valid_login():
    service = Service("../drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    login = LoginPage(driver)
    login.login("student", "Password123")

    time.sleep(2)
    assert "Logged In Successfully" in driver.page_source

    driver.quit()
