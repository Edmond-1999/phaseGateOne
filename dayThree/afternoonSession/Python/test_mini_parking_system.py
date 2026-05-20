from unittest import TestCase

import mini_parking_system

class TestCheckingASlot(TestCase):

    def test_that_checking_a_slot_exists(self):
        car_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        mini_parking_system.checking_a_slot(car_slots, 0)

    def test_that_checking_a_slot_returns_empty(self):
        car_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = "Empty"
        expected = mini_parking_system.checking_a_slot(car_slots, 1)
        self.assertEqual(actual, expected)

    def test_that_checking_a_slot_returns_occupied(self):
        car_slots = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = "Occupied"
        expected = mini_parking_system.checking_a_slot(car_slots, 1)
        self.assertEqual(actual, expected)

class TestParkingACar(TestCase):

    def test_that_parking_a_car_exists(self):
        car_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        mini_parking_system.parking_a_car(car_slots, 0)

    def test_that_parking_a_car_returns_now_occupied(self):
        car_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = mini_parking_system.parking_a_car(car_slots, 0)
        actual = "Now Occupied"
        self.assertEqual(actual, expected)

    def test_that_parking_a_car_returns_already_occupied_before_now(self):
        car_slots = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = mini_parking_system.parking_a_car(car_slots, 1)
        actual = "Already Occupied Before Now"
        self.assertEqual(actual, expected)

class TestUnparkingACar(TestCase):

    def test_that_unparking_a_car_exists(self):
        car_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        mini_parking_system.unparking_a_car(car_slots, 0)

    def test_that_unparking_a_car_returns_car_unparked(self):
        car_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = mini_parking_system.unparking_a_car(car_slots, 0)
        expected = "Car Unparked"
        self.assertEqual(actual, expected)


    def test_that_unparking_a_car_returns_car_not_yours(self):
        car_slots = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = mini_parking_system.unparking_a_car(car_slots, 1)
        expected = "Car Not Yours"
        self.assertEqual(actual, expected)


