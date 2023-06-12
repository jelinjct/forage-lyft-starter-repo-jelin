import unittest
from datetime import date
from battery.nubbinbattery import Nubbin_battery

class TestNubbin(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2024-09-10")
        last_service_date = date.fromisoformat("2020-05-20")
        battery=Nubbin_battery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())

class TestNubbin(unittest.TestCase):
    def test_needs_service_false(self):
        current_date = date.fromisoformat("2024-09-10")
        last_service_date = date.fromisoformat("2023-05-20")
        battery = Nubbin_battery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())