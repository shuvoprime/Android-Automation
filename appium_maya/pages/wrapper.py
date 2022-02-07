from appium import webdriver
#from appium.webdriver.common.by import By
#from appium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
import sys
sys.path.append(".")

class BasePage(object):
    
    def __init__(self, drv):
        self.drv = drv
    
    def wd_click_simple(self, locator):
        self.drv.find_element_by_xpath(locator).click()

    def wd_implicitly_wait(self, time):
        self.drv.implicitly_wait(time) 
                
    def wait_until_element_clickable(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))   
        return webel
    
    def wait_until_visibility_of_element_located(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))   
        return webel  
    
    def wait_until_visibility_of_element_located_CLASS_name(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))   
        return webel  

    def wait_until_visibility_of_element_located_name(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.NAME, locator)))   
        return webel

    def wd_Send_keys (self, locator, text):
        self.drv.find_element_by_xpath(locator).send_keys(Keys.CONTROL + "a")
        self.drv.find_element_by_xpath(locator).send_keys(text) 

    def wd_Send_keys_siimple (self, locator, text):
        self.drv.find_element_by_xpath(locator).send_keys(text) 
    
    def wd_Send_keys_Name (self, locator, text):
        self.drv.find_element(By.NAME, locator).clear()
        self.drv.find_element(By.NAME, locator).send_keys(text)    
    
    def wd_Send_keys_Name_simple (self, locator, text):
        self.drv.find_element(By.NAME, locator).send_keys(text)
    
    def wait_until_visibility_of_element_located_parameter(self, waitTime, search):
        locator = "//*div[contains(text(),{search})]".format(search)
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))   
        return webel 
               
    def wait_until_visibility_of_element_located_parameter(self, waitTime, container, search):
        locator = "//*div[contains({container},{search})]".format(container, search)
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))   
        return webel        
    
    def handle_webelement_exception(self, waitTime, locator,message ):   
        wait = WebDriverWait(self.drv, waitTime)
        try: 
            webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        except  NoSuchElementException:  
            print(message)
            
    def wait_untill_visibility_CSS(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))   
        return webel  
    
    def wd_click_simple_CSS_without_click(self,waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        #self.drv.find_element_by_css_selector(locator).click()   
    

    def wd_click_simple_CSS(self, locator):
        self.drv.find_element_by_css_selector(locator).click()   
    
        
    def findElementsimpleX(self, locator):
        webel =  self.drv.find_element_by_xpath(locator)
        return webel
    
    def Send_keys_inner_element(self, text, locator):
        webel = self.drv.find_element_by_xpath(locator)
        print(webel.text)
        webel.click()
        inner = webel.find_element_by_tag_name("input")
        time.sleep(2)
        inner.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + text)
        
        # inner.send_keys(text)
    
    def Send_keys_inner_element_clear(self, locator):
        webel = self.drv.find_element_by_xpath(locator)
        print(webel.text)
        webel.click()
        inner = webel.find_element_by_tag_name("input")
        inner.clear()
      
    def simpleXpath_with_click(self,locator):
        webel = self.drv.find_element_by_xpath(locator).click()
        return webel
        

    def get_title(self):
        webel = self.drv.title
        print(webel)
        return webel
    
    def is_visible(self, locator):
        elem = WebDriverWait(self.drv,10).until(EC.visibility_of_element_located(locator))
        return bool(elem)

    def handling_window(self):
        c_win_han = self.drv.current_window_handle
        chwnd = self.drv.window_handles
        #switch focus to child window
        for i in chwnd:
            if(i != c_win_han):
                self.drv.switch_to.window(i)
                break

    def handle_webelement_invisibility_timeout_exception(self, waitTime, locator, message):
        wait = WebDriverWait(self.drv, waitTime)
        try: 
            webel = wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))
        except  TimeOutException:  
            print(message)

    def wait_until_visibility_of_element_located_CLASS_NAME(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))   
        return webel 
    
    
    def wait_until_visibility_of_ALL_element_located_CLASS_NAME(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, locator)))   
        return webel 

    def wait_until_invisibility_of_element_located(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.invisibility_of_element_located((By.XPATH, locator)))   
        return webel 

    def scroll_to_specific_xpath(self, locator):
        #wait = WebDriverWait(self.drv, waitTime)
        webel = self.drv.find_element_by_xpath(locator)
        webel.location_once_scrolled_into_view
    
    def wd_list_of_elements (self, locator):
        webel = self.drv.find_elements_by_class_name(locator)
        return webel

    def app_wait_until_element_clickable_by_ID(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.element_to_be_clickable((By.ID, locator)))   
        return webel
    
    
    def app_wait_until_element_clickable_by_XPATH(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))   
        return webel