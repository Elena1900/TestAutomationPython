from pages.base_page import BasePage
from pages.locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def go_to_basket(self):
        self.browser.find_element(*BasketPageLocators.GO_TO_BASKET).click()


    def should_be_basket_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Item in the basket"


    def is_basket_empty(self):
        check_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert "Your basket is empty. Continue shopping" == check_text, "The basket is not empty"