from pom_framework.pages.basepage import BasePage
from selenium.webdriver.common.by import By


class AccountSummaryPage(BasePage):
    pay_bills_link = By.XPATH, "//a[text()='Pay Bills']"

    def click_pay_bills_link(self):
        self._click(self.pay_bills_link)
