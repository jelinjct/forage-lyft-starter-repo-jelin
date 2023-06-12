import unittest

from  tire.octoprime import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tearwear = [0.8,0.7,0.6,0.7]
        tire =  OctoprimeTires(tearwear)
        self.assertTrue(tire.needs_service())


    def test_needs_service_false(self):
        tearwear = [0.1,0.2,0.2,0.1]
        tire = OctoprimeTires(tearwear)
        self.assertFalse(tire.needs_service())