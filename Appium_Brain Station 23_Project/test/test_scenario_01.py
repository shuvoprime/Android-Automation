from pickle import TRUE
import pytest
from pages.scenario import scenario
import sys
sys.path.append(".")
import allure

@allure.severity(allure.severity_level.CRITICAL)
def test_moving_to_electronics(setup):
    global drv 
    drv = setup
    s1obj = scenario(drv)
    elem = s1obj.moving_to_electronics()
    assert elem == True
@allure.severity(allure.severity_level.NORMAL)
def test_going_to_nokia_lumia():
    s1obj = scenario(drv)
    elem = s1obj.going_to_nokia_lumia()
    assert elem == "Nokia Lumia 1020"

@allure.severity(allure.severity_level.CRITICAL)    
def test_updating_requirements():
    s1obj = scenario(drv)
    elem = s1obj.updating_requirements()
    assert elem[0] == '2'
    assert elem[1] == 'Large'
    assert elem[2] == True

@allure.severity(allure.severity_level.NORMAL)
def test_place_order_guest_user():
    s1obj = scenario(drv)
    elem = s1obj.place_order_guest_user()
    assert elem == True

@allure.severity(allure.severity_level.NORMAL)
def test_shipping_confirmation():
    s1obj = scenario(drv)
    elem = s1obj.shipping_confirmation()
    assert elem == True

@allure.severity(allure.severity_level.CRITICAL)
def test_payment_choose():
    s1obj = scenario(drv)
    elem = s1obj.payment_choose()
    assert elem == True

@allure.severity(allure.severity_level.NORMAL)
def test_payment_information_confirmation():
    s1obj = scenario(drv)
    elem = s1obj.payment_information_confirmation()
    assert elem == "Payment information" 

@allure.severity(allure.severity_level.NORMAL)
def test_confirmation_of_purchase():
    s1obj = scenario(drv)
    elem = s1obj.confirmation_of_purchase()
    assert elem == True
    
@allure.severity(allure.severity_level.NORMAL)
def test_tear_down(teardown):
    pass

