from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):
    def click_add_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)        
        btn.click() 
        #self.solve_quiz_and_get_code()    
    def check_name(self):
        time.sleep(2)
        abn = self.browser.find_element(*ProductPageLocators.ADD_BOOK_NAME)  
        bn =  self.browser.find_element(*ProductPageLocators.BOOK_NAME)  
        assert abn.text==bn.text, "Book name is not correct!"
    def check_price(self):        
        apr = self.browser.find_element(*ProductPageLocators.ADD_BOOK_PRICE)  
        pr =  self.browser.find_element(*ProductPageLocators.BOOK_PRICE)  
        assert apr.text==pr.text, f"Book price is not correct! {apr.text} and {pr.text}"    
    def should_not_be_success_message(self):                 
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"        
    def should_disappear_success_message(self):        
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"            
        
