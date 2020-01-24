import pytest
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    driver_ = webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com")

    def quit():
        # driver_.quit()
        pass

    request.addfinalizer(quit)

    return driver_
