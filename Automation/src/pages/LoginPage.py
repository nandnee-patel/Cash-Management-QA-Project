from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = "//input[@id='user']"
    password = "//input[@id='pass']"
    login_btn = "//button[@id='login']"

    def login(self, user, pwd):
        self.driver.find_element(By.XPATH, self.username).send_keys(user)
        self.driver.find_element(By.XPATH, self.password).send_keys(pwd)
        self.driver.find_element(By.XPATH, self.login_btn).click()
