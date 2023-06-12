
from serviceable import Serviceable

# new attribute called tire is added
class Car(Serviceable):
    def __init__(self, engine,battery):
        self.engine = engine
        self.battery=battery



    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
