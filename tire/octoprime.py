
from tire.octoprime import Tire


class OctoprimeTires(Tire):
    def __init__(self,tirewear):
        self.tirewear = tirewear

    def needs_service(self):
        if self.tirewear>=3.0:
            return True
        else:
            return False
