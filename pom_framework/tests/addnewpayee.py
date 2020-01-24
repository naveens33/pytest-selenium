import pytest

from pom_framework.pages.accountsummarypage import AccountSummaryPage
from pom_framework.pages.homepage import HomePage
from pom_framework.pages.loginpage import LoginPage
from pom_framework.pages.paybillspage import PayBillsPage
from pom_framework.testdata.read_excel_data import get_data


class Test_AddNewPayee:

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, driver):
        home = HomePage(driver)
        home.click_signin_button()
        login = LoginPage(driver)
        login.do_login("username", "password")
        acc = AccountSummaryPage(driver)
        acc.click_pay_bills_link()

    @pytest.fixture(autouse=True)
    def nav_to_anp(self, driver):
        self.paybills = PayBillsPage(driver)
        self.paybills.click_add_new_payee_link()

    @pytest.mark.parametrize("name,addrs,acc,details", get_data())
    def test_add_new_payee(self,name, addrs, acc, details):
        self.paybills.do_addnewpayee(name, addrs, acc, details)
