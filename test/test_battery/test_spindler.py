import unittest
from datetime import date
from battery.spindlerbattery import Spindler_battery

class TestSpindler(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2023-09-10")
        last_service_date = date.fromisoformat("2020-05-20")
        battery=Spindler_battery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())

class TestSpindler(unittest.TestCase):
    def test_needs_service_false(self):
        current_date = date.fromisoformat("2024-06-10")
        last_service_date = date.fromisoformat("2023-05-20")
        battery = Spindler_battery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())