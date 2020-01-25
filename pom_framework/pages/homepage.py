from pom_framework.pages.basepage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    signin_button = By.ID, "signin_button"
    feedback_link = By.XPATH, "//strong[text()='Feedback']"
    onlinebanking_link = By.XPATH, "//strong[text()='Online Banking']"

    def click_signin_button(self):
        self._click(self.signin_button)

    def click_onlinebanking_link(self):
        self._click(self.onlinebanking_link)