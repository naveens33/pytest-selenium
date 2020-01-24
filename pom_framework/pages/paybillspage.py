from pom_framework.pages.basepage import BasePage
from selenium.webdriver.common.by import By


class PayBillsPage(BasePage):
    add_new_payee_link = By.XPATH, "//a[text()='Add New Payee']"
    payee_name = By.ID, "np_new_payee_name"
    payee_address = By.ID, "np_new_payee_address"
    payee_account = By.ID, "np_new_payee_account"
    payee_details = By.ID, "np_new_payee_details"
    add_button = By.ID, "add_new_payee"

    def click_add_new_payee_link(self):
        self._click(self.add_new_payee_link)

    def do_addnewpayee(self, name, addrs, acc, details):
        self._wait_for_element(self.payee_name,"visibility").send_keys(name)
        self._enter_text(self.payee_address, addrs)
        self._enter_text(self.payee_account, acc)
        self._enter_text(self.payee_details, details)
        self._click(self.add_button)

