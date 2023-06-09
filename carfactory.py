from battery.nubbinbattery import Nubbin_battery
from battery.spindlerbattery import Spindler_battery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.type1 import Type1
from tire.type2 import Type2

from car import Car

class Carfactory:
    @staticmethod
    def create_calliope(current_date,last_service_date,current_mileage,last_service_mileage,airpressure_in_psi):
        engine=CapuletEngine(current_mileage,last_service_mileage)
        battery=Spindler_battery(current_date,last_service_date)
        tire=Type1(airpressure_in_psi)
        car=Car(engine,battery,tire)
        return car

    @staticmethod
    def create_glissade(current_date,last_service_date,current_mileage,last_service_mileage,airpressure_in_psi):
        engine=WilloughbyEngine(current_mileage,last_service_mileage)
        battery=Spindler_battery(current_date,last_service_date)
        tire = Type1(airpressure_in_psi)
        car=Car(engine,battery,tire)
        return car

    @staticmethod
    def create_palindrome(current_date,last_service_date,warning_light_is_on,airpressure_in_psi):
        engine=SternmanEngine(warning_light_is_on)
        battery=Spindler_battery(current_date,last_service_date)
        tire = Type1(airpressure_in_psi)
        car=Car(engine,battery,tire)
        return car

    @staticmethod
    def create_rorschach(current_date,last_service_date,current_mileage,last_service_mileage,airpressure_in_psi):
        engine=WilloughbyEngine(current_mileage,last_service_mileage)
        battery=Nubbin_battery(current_date,last_service_date)
        tire = Type2(airpressure_in_psi)
        car=Car(engine,battery,tire)
        return car

    @staticmethod
    def create_thovex(current_date,last_service_date,current_mileage,last_service_mileage,airpressure_in_psi):
        engine=CapuletEngine(current_mileage,last_service_mileage)
        battery=Nubbin_battery(current_date,last_service_date)
        tire = Type2(airpressure_in_psi)
        car=Car(engine,battery,tire)
        return car