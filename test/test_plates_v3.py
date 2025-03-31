""" 
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, 
restructuring your code per the below, wherein is_valid still expects a str as input and 
returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__"
 """
from plates_v3 import is_valid
import pytest


def test_length():
    with pytest.raises(SystemExit):
        is_valid('H') 
        is_valid('OUTATIME')
        is_valid('HELL223')

def test_banned_symbols():
    with pytest.raises(SystemExit):
        is_valid('PI3.14')

def test_invalid_numeral_suffix():
    with pytest.raises(SystemExit):
        is_valid('CS05')
        is_valid('CS50P')

def test_valid_values():
    assert is_valid('CS50') == 'Valid'
    assert is_valid('HE') == 'Valid'
    assert is_valid('HSG267') == 'Valid'


    
    