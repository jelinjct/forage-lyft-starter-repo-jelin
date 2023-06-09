from abc import ABC

from car import Car


class Type2(Car, ABC):
    def __init__(self,airpressure_in_psi):
        self.airpressure_in_psi = airpressure_in_psi

    def needs_service(self):
        if self.airpressure_in_psi<70:
            return True
        else:
            return False
