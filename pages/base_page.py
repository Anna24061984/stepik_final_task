from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators, BasketPageLocators
import math
import time
import pyperclip

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)    
    
    def open(self):
        self.browser.get(self.url)
        
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"    
        
    def go_to_basket(self):                     #С главной или со страницы продукта можно перейти в корзину
        btn = self.browser.find_element(*BasketPageLocators.BASKET_BTN)
        btn.click()
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True    
    
    def is_not_element_present(self, how, what, timeout=4):              
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True            
        return False  
        
    def is_disappeared(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True       
        
    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())        
        alert = self.browser.switch_to.alert        
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)        
        alert.accept()        
        try:
            WebDriverWait(self.browser, 3).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            pyperclip.copy(alert.text.split(" ")[-1])
            print(f"Your code: {alert_text}")
            alert.accept()
            #time.sleep(50)
        except (NoAlertPresentException, TimeoutException):
            print("No second alert presented")  
            
         
    