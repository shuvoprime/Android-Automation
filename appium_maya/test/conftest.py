import pytest
from appium import webdriver
import sys
sys.path.append(".")
from appium import webdriver
#from appium.webdriver.common.mobileby import MobileBy
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.wrapper import BasePage
from resources.locators import common_locators as cl

@pytest.fixture
def setup():
    global driver
    dc = {}
    dc['deviceName'] = "R58RA1592KB"
    dc['platformName'] = "Android"
    dc['app'] = ""
    dc['appPackage'] = ""
    dc['appActivity'] = ""
    
    driver = webdriver.Remote("", dc)

    wrap = BasePage(driver)
    wrap.app_wait_until_element_clickable_by_ID(10, cl.skip_tour_id).click()
    wrap.app_wait_until_element_clickable_by_ID(10, cl.language_dropdown_bar_id).click()
    wrap.app_wait_until_element_clickable_by_ID(10, cl.language_english_radio_button_id).click()
    wrap.app_wait_until_element_clickable_by_ID(10, cl.language_ok_button_id).click()
    time.sleep(3)
    return driver

@pytest.fixture
def teardown():
    driver.close_app()
    driver.quit()
    return teardown

