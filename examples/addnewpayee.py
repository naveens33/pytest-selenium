import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from parametrize_example.read_excel_data import get_data

class Test_AddNewPayee:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self, driver):
        driver.find_element_by_xpath("//a[text()='Pay Bills']").click()

    @pytest.fixture(autouse=True)
    def nav_to_anp(self,driver):
        driver.find_element_by_xpath("//a[text()='Add New Payee']").click()

    @pytest.mark.parametrize("name,addrs,acc,details", get_data())
    def test_01(self, driver, name, addrs, acc, details):
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, "np_new_payee_name"))).send_keys(name)
        driver.find_element_by_id("np_new_payee_address").send_keys(addrs)
        driver.find_element_by_id("np_new_payee_account").send_keys(acc)
        driver.find_element_by_id("np_new_payee_details").send_keys(details)
        driver.find_element_by_id("add_new_payee").click()
