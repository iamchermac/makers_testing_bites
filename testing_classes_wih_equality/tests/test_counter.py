from lib.counter import *

def test_counter_can_count_to_5():
    ticker = Counter()
    for i in range(1,6):
        ticker.add(1)
    
    response = ticker.report()
    criteria = "Counted to 5 so far."
    
    assert response == criteria
    