""" 
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert expects a str in X/Y format as input, wherein each of X and Y is an integer, 
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. 
If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. 
If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
 """


from fuel_v2 import convert 
from fuel_v2 import gauge


def test_tank_full_fraction():
    assert convert("5/5") == 'F'
    assert convert("99/100") == 'F'

def test_tank_empty_fraction():
    assert convert("1/100") == 'E'
    assert convert("0/100") == 'E'

def test_others_fraction():
    assert convert("5/10") == "Fuel Available:  50.00%"
    assert convert("3/4") == "Fuel Available:  75.00%"

def test_tank_full():
    assert gauge(5/5) == 100
    assert gauge(99/100) == 99

def test_tank_empty():
    assert gauge(1/100) == 1
    assert gauge(0/10) == 0

def test_others():
    assert gauge(5/10) == 50
    assert gauge(3/4) == 75
