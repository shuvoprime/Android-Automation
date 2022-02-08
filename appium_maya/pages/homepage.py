from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
#this touch action library  is for scrolling  and swiping
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys
sys.path.append(".")
from pages.wrapper import BasePage
from resources.locators import homepage_locators as hl

class homepage(BasePage):
        
    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)

    def header_check(self):
        wrap = self.Wrap
        elem = wrap.app_wait_until_element_clickable_by_ID(10, hl.homepage_header_id)
        return elem.text

    def expert_list_visibility(self):
        wrap = self.Wrap
        wrap.app_swipe_v3(320,1202,358,540)
        elem = wrap.app_wait_until_element_clickable_by_XPATH(20 , hl.homepage_expert_list_xpath)
        return elem.text
    
    def featured_question_visibility(self):
        wrap = self.Wrap
        elem = wrap.app_wait_until_element_clickable_by_XPATH(20, hl.homepage_feature_question_xpath)
        return elem.text
    
    def play_quiz_visibility(self):
        wrap = self.Wrap
        wrap.app_swipe_v3(299,1277,362,199)
        elem = wrap.app_wait_until_element_clickable_by_XPATH(20, hl.homepage_play_quiz_xpath)
        return elem.text
    
    def trending_now_visibility(self):
        wrap = self.Wrap
        elem = wrap.app_wait_until_element_clickable_by_XPATH(20, hl.homepage_trending_now_xpath)
        return elem.text