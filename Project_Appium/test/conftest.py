import pytest
from appium import webdriver
import sys
sys.path.append(".")
from appium import webdriver
#from appium.webdriver.common.mobileby import MobileBy
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.wrapper import BasePage
from resources.locators import common_locators as cl

@pytest.fixture
def setup():
    global driver
    dc = {}
    #dc['deviceName'] = "R58RA1592KB"
    dc['deviceName'] = "emulator-5554"
    dc['platformName'] = "Android"
    dc['app'] = "C:\\Users\\shuvo\\AppData\\Local\\Android\\Sdk\\app\\nopstationCart_4.40.apk"
    dc['appWaitPackage'] = "com.nopstation.nopcommerce.nopstationcart"
    dc['appWaitActivity'] = "com.bs.ecommerce.main.SplashScreenActivity"
    
    driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.ID, cl.button_terms_condition_id))).click()
    time.sleep(5)
    return driver

@pytest.fixture
def teardown():
    driver.close_app()
    driver.quit()
    return teardown
'''
setup()
teardown()
'''