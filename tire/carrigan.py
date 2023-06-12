
from tire.tire import Tire


class CarriganTires(Tire):
    def __init__(self,tirewear):
        self.tirewear = tirewear

    def needs_service(self):
        for i in self.tirewear:
                if i>=0.9:
                    return True
        return False
