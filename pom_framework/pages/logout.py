from pom_framework.pages.basepage import BasePage
from selenium.webdriver.common.by import By


class LogoutPage(BasePage):
    username_link = By.XPATH, "(//a[@class='dropdown-toggle'])[2]"
    logout_link = By.XPATH, "//a[text()='Logout']"


    def do_logout(self):
        self._click(self.username_link)
        self._click(self.logout_link)
