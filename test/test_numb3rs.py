from numb3rs import validate

def test_valid_ip():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("0.10.200.1") == True
    
def test_invalid_ip():
    assert validate("cat") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("0222.2.3.100") == False