import random
letters = "ABCDEFGHIJKMNLOPQRSTUVWXYZ"
numbers = "1234567890"

# random.seed(2)

def license_plate_generator():
    plate_number = []
    for i in range(3):
        plate_number.append(random.choice(letters))
    plate_number.append(" ")
    for i in range(4):
        plate_number.append(random.choice(numbers))

    plate_number_string = "".join(plate_number)
    return plate_number_string

print(license_plate_generator() )
                            
