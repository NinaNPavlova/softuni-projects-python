import unittest
from project.second_hand_car import SecondHandCar

class TestSecondHandCar(unittest.TestCase):

    def setUp(self):
        self.car = SecondHandCar("BMW", "Sedan", 150, 5000)

    def test_init(self):
        self.assertEqual("BMW", self.car.model)
        self.assertEqual("Sedan", self.car.car_type)
        self.assertEqual(150, self.car.mileage)
        self.assertEqual(5000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1.0
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

    def test_mileage_setter_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

    def test_set_promotional_price_invalid(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(6000)
        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_set_promotional_price_valid(self):
        result = self.car.set_promotional_price(4000)
        self.assertEqual('The promotional price has been successfully set.', result)
        self.assertEqual(4000, self.car.price)

    def test_need_repair_price_too_high(self):
        result = self.car.need_repair(3000, "Engine fix")
        self.assertEqual('Repair is impossible!', result)
        self.assertEqual([], self.car.repairs)

    def test_need_repair_success(self):
        result = self.car.need_repair(2000, "Front bumper")
        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertEqual(7000, self.car.price)
        self.assertIn("Front bumper", self.car.repairs)

    def test_compare_different_type(self):
        other = SecondHandCar("Audi", "Coupe", 200, 4000)
        result = self.car > other
        self.assertEqual('Cars cannot be compared. Type mismatch!', result)

    def test_compare_valid(self):
        other = SecondHandCar("Audi", "Sedan", 200, 4000)
        self.assertTrue(self.car > other)

    def test_str(self):
        expected = """Model BMW | Type Sedan | Milage 150km
Current price: 5000.00 | Number of Repairs: 0"""
        self.assertEqual(expected, str(self.car))

if __name__ == "__main__":
    unittest.main()