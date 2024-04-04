import pytest
from lib.password_checker import *

def test_password_has_10_chars_returns_True():
    criteria = True
    
    validator = PasswordChecker()
    response = validator.check("Donatello")
    
    assert response == criteria

def test_password_has_7_chars_returns_Exception():
    criteria = "Invalid password, must be 8+ characters."
    
    validator = PasswordChecker()
    with pytest.raises(Exception) as err:
        validator.check("Bob")
    response = str(err.value)
    
    assert response == criteria
    