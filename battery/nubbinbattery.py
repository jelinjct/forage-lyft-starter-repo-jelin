from battery.battery import Battery
from date import add_years_to_date


class Nubbin_battery(Battery):
    def __int__(self,current_date,last_service_date):
        self.current_date=current_date
        self.last_service_date=last_service_date
    def needs_service(self):
        service_duedate= add_years_to_date(self.last_service_date,4)
        if service_duedate<self.current_date:
            return True
        else:
            return False