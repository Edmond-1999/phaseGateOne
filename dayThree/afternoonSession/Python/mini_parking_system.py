car_slots = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def checking_a_slot(car_slots, slot_number):

    if car_slots[slot_number] == 0:
        return "Empty"
    elif car_slots[slot_number] == 1:
        return "Occupied"

def parking_a_car(car_slots, slot_number):
    checking_slot = checking_a_slot(car_slots, slot_number)

    if checking_slot == "Empty":
        car_slots[slot_number] = 1
        return "Now Occupied"
    else:
        return "Already Occupied Before Now"


def unparking_a_car(car_slots, slot_number):
    parking_car = parking_a_car(car_slots, slot_number)

    if parking_car == "Now Occupied":
        car_slots[slot_number] = 0
        return "Car Unparked"
    elif parking_car == "Already Occupied Before Now":
        return "Car Not Yours"


