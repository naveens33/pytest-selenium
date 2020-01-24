from pom_framework.pages.basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    uname_input = By.ID, "user_login"
    pword_input = By.ID, "user_password"
    signin_button = By.NAME, "submit"

    def do_login(self, uname, pword):
        self._enter_text(self.uname_input, uname)
        self._enter_text(self.pword_input, pword)
        self._click(self.signin_button)
