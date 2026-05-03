from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.checkout_button = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.success_message = (By.CLASS_NAME, "complete-header")

    def start_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()

    def enter_details(self, fname, lname, zip_code):
        self.wait.until(EC.visibility_of_element_located(self.first_name)).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)

        self.driver.find_element(*self.continue_button).click()

        # WAIT for next page (overview page)
        self.wait.until(EC.visibility_of_element_located(self.finish_button))

    def finish_order(self):
        self.wait.until(EC.element_to_be_clickable(self.finish_button)).click()

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_message)).text