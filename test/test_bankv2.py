""" 
In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, 
restructuring your code per the below, wherein value expects a str as input and returns an int, namely 
0 if that str starts with “hello”, 
20 if that str starts with an “h” (but not “hello”), 
or 100 otherwise, treating the str case-insensitively. 
You can assume that the string passed to the value function will not contain any leading spaces. 
Only main should call print.
 """

from bank_v2 import value

def test_greeting_with_hello():
    assert value("hello") == 0
    assert value("hello, Newman") == 0

def test_greeting_with_h():    
    assert value("how you doing?") == 20
    assert value("hi?") == 20
    

def test_greeting_without_above():
    assert value("What's happening?") == 100
