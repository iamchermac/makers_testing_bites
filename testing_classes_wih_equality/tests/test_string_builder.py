from lib.string_builder import *

def test_size_of_hello_world_returns_11():
    criteria = 11
    
    concatenator = StringBuilder()
    concatenator.add("hello")
    concatenator.add(" ")
    concatenator.add("world")
    
    response = concatenator.size()
    
    assert response == criteria

def test_output_returns_hello_world():
    criteria = "hello world"
    
    concatenator = StringBuilder()
    concatenator.add("hello")
    concatenator.add(" ")
    concatenator.add("world")
    
    response = concatenator.output()
    
    assert response == criteria
    