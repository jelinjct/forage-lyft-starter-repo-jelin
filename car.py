from abc import ABC, abstractmethod

# new attribute called tire is added
class Car(ABC):
    def __init__(self, engine,battery,tire):
        self.engine = engine
        self.battery=battery
        self.tire=tire

    @abstractmethod
    def needs_service(self):
        pass
