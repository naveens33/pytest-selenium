from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    driver = None

    def __init__(self, d):
        self.driver = d

    def _click(self, locator):
        self.driver.find_element(*locator).click()

    def _enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def _get_elements(self,locator):
        return self.driver.find_elements(*locator)

    def _wait_for_element(self, locator, condition):
        wait = WebDriverWait(self.driver, 5)
        if condition == "visibility":
            return wait.until(EC.visibility_of_element_located(locator))
        elif condition == "clickable":
            return wait.until(EC.element_to_be_clickable(locator))

    def _wait_for_elements(self, locator, condition):
        wait = WebDriverWait(self.driver, 5)
        if condition == "visibility":
            return wait.until(EC.visibility_of_all_elements_located(locator))

