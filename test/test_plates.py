""" 
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, 
restructuring your code per the below, wherein is_valid still expects a str as input and 
returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__"
 """
from plates_v2 import is_valid

def test_length():
    assert is_valid('H') == 'Invalid'
    assert is_valid('OUTATIME') == 'Invalid'
    assert is_valid('HELL223') == 'Invalid'

def test_banned_symbols():
    assert is_valid('PI3.14') == 'Invalid'

def test_invalid_numeral_suffix():
    assert is_valid('CS05') == 'Invalid'
    assert is_valid('CS50P') == 'Invalid'

def test_valid_values():
    assert is_valid('CS50') == 'Valid'
    assert is_valid('HE') == 'Valid'
    assert is_valid('HSG267') == 'Valid'


    
    