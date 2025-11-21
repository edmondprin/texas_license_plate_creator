'''
The result length is correct
The first 3 characters are A–Z
The last 4 characters are digits
The function returns a string
Optional: generated plates are unique over multiple calls
Optional: edge cases (like seeding the RNG)
'''
import random
from texas_plate_generator import license_plate_generator

random.seed(123)



def test_license_plate_len():
    plate = license_plate_generator()
    assert len(plate) == 8

def test_license_plate_ch():
    plate = license_plate_generator()
    assert plate[:3].isupper() and plate[:3].isalpha()
    assert ord(plate[3]) == 32
    assert plate[3] == " "
    assert plate[4:].isdigit()

def test_license_plate_type():
    plate = license_plate_generator()
    assert type(plate) == str
    assert isinstance(plate, str)


def test_multiple_calls():
    plates_list = []
    for i in range(100):
        plate = license_plate_generator()
        plates_list.append(plate)
    assert len(set(plates_list)) >= 2
        
