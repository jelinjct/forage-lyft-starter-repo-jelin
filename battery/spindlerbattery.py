from battery.battery import Battery
from date import add_years_to_date


class Spindler_battery(Battery):
    def __int__(self,current_date,last_service_date):
        self.current_date=current_date
        self.last_service_date=last_service_date
    def needs_service(self):
        x= add_years_to_date(self.last_service_date,2)
        if x<self.current_date:
            return True
        else:
            return False