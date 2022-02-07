import pytest
from pages.homepage import homepage
import sys
sys.path.append(".")


def test_homepage_header_checker(setup):
    global drv 
    drv = setup
    homeobj = homepage(drv)
    elem = homeobj.header_check()

    if "Hello" in elem:
      assert True
    else:
      assert False

def test_tear_down(teardown):
    pass