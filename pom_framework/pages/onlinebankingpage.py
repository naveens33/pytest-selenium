from pom_framework.pages.basepage import BasePage
from selenium.webdriver.common.by import By


class OnlineBankingPage(BasePage):
    features_links = By.XPATH, "//div[@id='online_banking_features']//span"

    def click_feature_link(self,name):
        elements = self._get_elements(self.features_links)
        for element in elements:
            if element.text == name:
                element.click()
                break
        else:
            print("Feature not found")