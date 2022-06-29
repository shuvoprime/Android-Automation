from textwrap import wrap
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import pytest
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
from resources.locators import lumia_update as lu
from resources.locators import payment as p
import xlrd


class scenario(BasePage):
        
    def __init__ (self,drv):
        self.drv = drv
        self.Wrap = BasePage(self.drv)

    def moving_to_electronics(self):
        wrap = self.Wrap
        #time.sleep(3)
        wrap.app_swipe(1016,1027,60,970)
        wrap.app_swipe(987,1018,269,1056)
        elem = wrap.app_wait_until_element_visible_by_XPATH(10,hl.electronics_xpath_v2)
        return bool(elem)

    def going_to_nokia_lumia(self):
        wrap = self.Wrap
        elem = wrap.app_wait_until_element_clickable_by_XPATH(10, hl.electronics_xpath_v2).click()
        time.sleep(2)
        wrap.app_swipe(538,1740,529,690)
        time.sleep(2)
        wrap.app_swipe(538,1952,602,899)
        wrap.app_wait_until_element_clickable_by_XPATH(10, hl.lumia_xpath).click()
        elem = wrap.app_wait_until_element_visible_by_ID(20 , hl.lumia_inside_id)
        return elem.text

    
    def updating_requirements(self):
        wrap = self.Wrap
        wrap.app_swipe_v3(569,1409,538,1046)
        wrap.app_wait_until_element_clickable_by_ID(10, lu.quatity_increase_id).click()
        elem = wrap.app_wait_until_element_visible_by_ID(10, lu.quantity_text_increase_id)
        wrap.app_wait_until_element_clickable_by_XPATH(10, lu.size_select_xpath).click()
        #time.sleep(3)
        wrap.app_wait_until_element_clickable_by_XPATH(10,lu.size_large_xpath).click()
        #time.sleep(3)
        wrap.app_wait_until_element_clickable_by_XPATH(10,lu.size_large_text_xpath).click()
        #time.sleep(3)
        elem1 = wrap.app_wait_until_element_visible_by_XPATH(10,lu.size_large_text_xpath)
        wrap.app_wait_until_element_clickable_by_ID(10,lu.add_to_cart_button_id).click()
        elem2 = wrap.app_wait_until_element_visible_by_ID(10, lu.add_to_cart_confirm_text_id)
        return elem.text,elem1.text,bool(elem2)

    def place_order_guest_user(self):
        wrap = self.Wrap
        wrap.app_wait_until_element_clickable_by_ID(10,lu.cart_icon_click_id).click()
        time.sleep(2)
        wrap.app_wait_until_element_clickable_by_XPATH(10,lu.checkout_xpath_v1).click()
        time.sleep(2)
        wrap.app_wait_until_element_clickable_by_XPATH(10, lu.checkout_guest_xpath).click()
        
        #adding data from excel
        path = ("C:\Users\shuvo\Desktop\BS23\excel\datasheet.xls")
        workbook = xlrd.open_workbook(path)
        worksheet = workbook.sheet_by_index(0)

        time.sleep(2)
        wrap.app_wait_until_element_visible_by_ID(10, p.first_name_id).send_keys(worksheet.cell_value(1,0))
        wrap.app_wait_until_element_visible_by_ID(10, p.last_name_id).send_keys(worksheet.cell_value(1,1))
        wrap.app_wait_until_element_visible_by_ID(10, p.email_id).send_keys(worksheet.cell_value(1,2))
        wrap.app_wait_until_element_visible_by_ID(10, p.select_country_dropdown_id).click()
        
        time.sleep(1)
        wrap.app_swipe(545,2142,551,1037)
        time.sleep(1)
        wrap.app_swipe(545,2158,532,425)
        wrap.app_wait_until_element_visible_by_XPATH(10, p.select_country_xpath).click()
        wrap.app_wait_until_element_visible_by_XPATH(10, p.select_state_xpath).click()
        wrap.app_wait_until_element_visible_by_XPATH(10, p.select_state_other_xpath).click()

        wrap.app_wait_until_element_visible_by_ID(10,p.company_id).send_keys(worksheet.cell_value(1,3))
        wrap.app_wait_until_element_visible_by_ID(10,p.city_id).send_keys(worksheet.cell_value(1,4))
        wrap.app_wait_until_element_visible_by_ID(10,p.street_id).send_keys(worksheet.cell_value(1,5))
        wrap.app_swipe(557,2006,507,710)
        wrap.app_wait_until_element_visible_by_ID(10,p.zip_id).send_keys(worksheet.cell_value(1,6))

        elem = wrap.app_wait_until_element_visible_by_ID(10,p.continue_button_id)
        wrap.app_wait_until_element_clickable_by_ID(10,p.continue_button_id).click()
        return bool(elem)

    def shipping_confirmation(self):
        wrap = self.Wrap
        elem = wrap.app_wait_until_element_visible_by_XPATH(10, p.next_air_day_xpath)
        wrap.app_wait_until_element_clickable_by_XPATH(10 , p.next_air_day_xpath).click()
        time.sleep(2)
        wrap.app_swipe(545,1978,526,691)
        wrap.app_wait_until_element_visible_by_XPATH(10 , p.continue_shipping_xpath).click()
        return bool(elem)

    def payment_choose(self):
        wrap = self.Wrap
        time.sleep(3)
        wrap.app_swipe(554,1967,507,482)
        time.sleep(1)
        wrap.app_swipe(529,2012,500,488)
        time.sleep(1)
        wrap.app_swipe(519,2012,469,601)

        wrap.app_wait_until_element_clickable_by_ID(10, p.check_money_order_payment_id).click()
        elem = wrap.app_wait_until_element_visible_by_ID(10, p.check_money_order_payment_id)
        wrap.app_wait_until_element_clickable_by_XPATH(10, p.check_money_order_payment_confirm_xpath).click()
        return  bool(elem)

    def payment_information_confirmation(self):
        wrap = self.Wrap
        time.sleep(3)
        elem = wrap.app_wait_until_element_visible_by_XPATH(10,p.payment_information_header_xpath)
        wrap.app_wait_until_element_clickable_by_XPATH(10, p.payment_info_next_xpath).click()
        return elem.text

    def confirmation_of_purchase(self):
        wrap = self.Wrap
        time.sleep(5)
        wrap.app_wait_until_element_clickable_by_XPATH(10, p.final_confirm_button_xpath).click()
        time.sleep(5)
        wrap.app_wait_until_element_clickable_by_ID(10, p.successful_continue_button_id).click()
        time.sleep(5)
        elem = wrap.app_wait_until_element_visible_by_ID(10 , p.after_success_main_page_header_id)
        return bool(elem)

