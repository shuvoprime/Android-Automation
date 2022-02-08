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

def test_our_expert_list_visibility():
    homeobj = homepage(drv)
    elem = homeobj.expert_list_visibility()
    assert elem == "Our experts are ready to help you"


def test_featured_question_visibility():
    homeobj = homepage(drv)
    elem = homeobj.featured_question_visibility()
    assert elem == "Featured question"

def test_play_quiz_visibility():
    homeobj = homepage(drv)
    elem = homeobj.play_quiz_visibility()
    assert elem == "Play quiz and learn"

def test_trending_now_question_visibility():
    homeobj = homepage(drv)
    elem = homeobj.trending_now_visibility()
    assert elem == "Trending now"



def test_tear_down(teardown):
    pass
