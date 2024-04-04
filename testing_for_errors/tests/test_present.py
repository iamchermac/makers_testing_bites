import pytest
from lib.present import *

def test_the_contents_returns_None():
    criteria = None
    
    xmas_gift = Present()
    response = xmas_gift.contents
    
    assert response == criteria

def test_wrapping_returns_bike():
    criteria = "bike"
    
    xmas_gift = Present()
    xmas_gift.wrap("bike")
    response = xmas_gift.unwrap()
    
    assert response == criteria

def test_unwrap_None_returns_Exception():
    criteria = "No contents have been wrapped."
    
    xmas_gift = Present()
    with pytest.raises(Exception) as err:
        xmas_gift.unwrap()
    response = str(err.value)
    
    assert response == criteria

def test_wrap_bike_then_car_returns_Exception():
    criteria = "A contents has already been wrapped."
    
    xmas_gift = Present()
    xmas_gift.wrap("bike")
    with pytest.raises(Exception) as err:
        xmas_gift.wrap("car")
    response = str(err.value)
    
    assert response == criteria