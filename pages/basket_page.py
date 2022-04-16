from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):       
    #def should_be_empty(self):                 
    #    assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"        
    def should_be_message_about_empty(self):                
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "There is no message that basket is empty."  
    def should_be_empty_list_of_products(self):                
        assert self.is_not_element_present(*BasketPageLocators.ANY_PRODUCT), "There is no message that basket is empty."  