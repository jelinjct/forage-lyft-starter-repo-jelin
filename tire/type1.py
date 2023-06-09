
from tire.tire import Tire


class Type1(Tire):
    def __init__(self,airpressure_in_psi):
        self.airpressure_in_psi = airpressure_in_psi

    def needs_service(self):
        if self.airpressure_in_psi<50:
            return True
        else:
            return False
