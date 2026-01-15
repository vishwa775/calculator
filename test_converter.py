from converter import celsius_to_fahrenheit

def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32

def test_positive_celsius():
    assert celsius_to_fahrenheit(100) == 212

def test_negative_celsius():
    assert celsius_to_fahrenheit(-40) == -40
