from response import syntax_validation_for_email

def test_valid_email_patterns():
    assert syntax_validation_for_email("malan@harvard.edu") == True
    assert syntax_validation_for_email("malan@harvard.ac.com") == True
    assert syntax_validation_for_email("dee.ve2023@aut.ac.nz") == True
    assert syntax_validation_for_email("dee_VE2023@aut.ac.nz") == True
    assert syntax_validation_for_email("dee-VE2023@aut.ac.nz") == True

def test_invalid_email_patterns():
    assert syntax_validation_for_email("malan@@@harvard.edu") == False
    assert syntax_validation_for_email("malan@harvard.ac..com") == False
    assert syntax_validation_for_email("malan@harvard.ac.com!") == False
    