import unittest

from  tire.carrigan import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tirewear = [0.9,0.8,0.2,0.1]
        tire =  CarriganTires(tirewear)
        self.assertTrue(tire.needs_service())


    def test_needs_service_false(self):
        tirewear = [0.4,0.2,0.2,0.1]
        tire = CarriganTires(tirewear)
        self.assertFalse(tire.needs_service())