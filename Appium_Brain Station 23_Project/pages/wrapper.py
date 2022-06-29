from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
#this touch action library  is for scrolling  and swiping

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import sys
sys.path.append(".")

class BasePage(object):
    
    def __init__(self, drv):
        self.drv = drv
    
    def app_wait_until_element_visible_by_ID(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.ID, locator)))   
        return webel

    def app_wait_until_element_clickable_by_XPATH(self, waitTime,Locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.element_to_be_clickable((By.XPATH, Locator)))   
        return webel
    
    def app_wait_until_element_visible_by_XPATH(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))   
        return webel

    def app_swipe(self,x1,y1,x2,y2):
        return TouchAction(self.drv).press(x= x1,y=y1).wait(2000).move_to(x=x2, y=y2).release().perform()
        

    def app_swipe_v3(self,start_X,start_Y,end_X,end_Y):
        return self.drv.swipe(start_X,start_Y,end_X,end_Y)
    
    def app_all_web_elements_parse_by_CLASS(self, waitTime, locator):
        wait = WebDriverWait(self.drv, waitTime)
        webel = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, locator)))   
        return webel

    def app_tap_by_coordinate(self,x1,y1):
        return TouchAction(self.drv).press(x = x1,y=y1).wait(2000).release().perform()
    