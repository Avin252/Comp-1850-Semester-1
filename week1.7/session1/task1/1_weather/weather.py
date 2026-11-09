"""
Module of weather-related functions.
"""

def comfort_level(temperature):
    """
    Given temperature in degrees Celsius, returns an indication of comfort
    level as a string ("COLD", "OK" or "HOT").
    """
    if temperature <= 15.0:
        return "COLD"
    elif temperature > 25.0:
        return "HOT"
    else:
        return "OK"
def test_cold():
    assert comfort_level(10.0) == "COLD"
    assert comfort_level(15.0) == "COLD"
def test_ok():
    assert comfort_level(20.0) == "OK"
    assert comfort_level(25.0) == "OK"
def test_hot():
    assert comfort_level(30.0) == "HOT"
    assert comfort_level(26.0) == "HOT"
