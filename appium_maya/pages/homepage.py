from appium import webdriver
#from appium.webdriver.common.mobileby import By
#from appium.webdriver.common.keys import Keys
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