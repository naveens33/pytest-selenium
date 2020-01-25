import pytest
from selenium import webdriver

from _pytest.runner import runtestprotocol
from ctreport_selenium.ctlistener import Session


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    driver_ = webdriver.Chrome(r"D:/Naveen/Selenium/chromedriver_win32/chromedriver.exe")
    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com")
    session_details = {
        "owner": "Naveen S",
        "environment": "QA",
        "browser": "chrome 79",
        "application name": "Zero Bank",
        "os": "Windows 10",
    }
    path = r"C:\Users\naveen.s\PycharmProjects\pytest-tutorial\pom_framework\reports"
    logo_path = r"C:\Users\naveen.s\PycharmProjects\pytest-tutorial\pom_framework\download.jpeg"

    Session.start("Smoke Test- Zero Bank", path, driver, logo_path, session_details)

    def quit():
        # driver_.quit()
        pass

    request.addfinalizer(quit)

    return driver_

def pytest_runtest_protocol(item, nextitem):
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when== 'setup':
            test = item.cls.test
        if report.when == 'call':
            if report.outcome == 'skipped':
                test.skip(report.longrepr[2])
            if report.outcome == 'failed':
                test.broken(report.longrepr.reprcrash.message)
        if report.when == 'teardown':
            test.finish()
    return False

def pytest_sessionfinish(session):
    Session.end()