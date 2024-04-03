from lib.gratitudes import *

def test_gratitude_for_apples():
    criteria = "Be grateful for: apples"
    
    gracious = Gratitudes()
    gracious.add("apples")
    response = gracious.format()
    
    assert response == criteria

def test_gratitude_for_animals():
    criteria = "Be grateful for: lions, tigers, bears, oh my!"
    
    gracious = Gratitudes()
    gracious.add("lions")
    gracious.add("tigers")
    gracious.add("bears")
    gracious.add("oh my!")
    response = gracious.format()
    
    assert response == criteria