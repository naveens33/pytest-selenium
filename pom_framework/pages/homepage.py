from pom_framework.pages.basepage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    signin_button = By.ID, "signin_button"
    feedback_link = By.XPATH, "//strong[text()='Feedback']"

    def click_signin_button(self):
        self._click(self.signin_button)
