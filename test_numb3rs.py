from numb3rs import validate

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3.4.4") == False
    assert validate("256.2.3.4") == False
    assert validate("75.456.76.65") == False
