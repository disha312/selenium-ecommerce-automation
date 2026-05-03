from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

logger = get_logger()

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        logger.info("Opening SauceDemo login page")
        self.driver.get("https://www.saucedemo.com/")


    def login(self, user, pwd):
        logger.info("Entering username")
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(user)

        logger.info("Entering password")
        self.driver.find_element(*self.password).send_keys(pwd)

        logger.info("Clicking login button")
        self.driver.find_element(*self.login_button).click()