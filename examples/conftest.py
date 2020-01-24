import pytest
from selenium import webdriver

@pytest.fixture(scope="session", autouse=True)
def driver(request):
    driver_ = webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com")
    driver_.find_element_by_id("signin_button").click()
    driver_.find_element_by_id("user_login").send_keys("username")
    driver_.find_element_by_id("user_password").send_keys("password")
    driver_.find_element_by_name("submit").click()
    driver_.find_element()
    def quit():
        #driver_.quit()
        pass
    request.addfinalizer(quit)

    return driver_