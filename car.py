from abc import ABC, abstractmethod
from datetime import date


class EngineBaseClass(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass


class CapuletEngine(EngineBaseClass):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage: int = last_service_mileage
        self.current_mileage: int = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000


class WilloughbyEngine(EngineBaseClass):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage: int = last_service_mileage
        self.current_mileage: int = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000


class SternmanEngine(EngineBaseClass):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on: bool = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on


class BatteryBaseClass(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass


class SpindlerBattery(BatteryBaseClass):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date: date = last_service_date
        self.current_date: date = current_date

    def needs_service(self) -> bool:
        date_of_expiry = self.last_service_date.replace(
            year=self.last_service_date.year + 2)
        return date_of_expiry < self.current_date


class NubbinBattery(BatteryBaseClass):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date: date = last_service_date
        self.current_date: date = current_date

    def needs_service(self) -> bool:
        date_of_expiry = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        return date_of_expiry < self.current_date


class Car():
    def __init__(self, Engine: EngineBaseClass, Battery: BatteryBaseClass):
        self.engine: EngineBaseClass = Engine
        self.battery: BatteryBaseClass = Battery

    def needs_service(self) -> bool:
        toReturn = False
        engine_needs_service = self.engine.needs_service()
        if engine_needs_service:
            toReturn = True
        battery_needs_service = self.battery.needs_service()
        if battery_needs_service:
            toReturn = True

        return toReturn


class CarFactory():

    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        """ Create a Calliope with a Capulet Engine and Spindler Battery """
        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date)
        )

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        """ Create a Glissade with a Willoughby Engine and Spindler Battery """
        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date)
        )

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        """ Create a Palindrome with a Sternman Engine and Spindler Battery """
        return Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(last_service_date, current_date)
        )

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        """ Create a Rorschach with a Willoughby Engine and Nubbin Battery """
        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date)
        )

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        """ Create a Thovex with a Capulet engine and Nubbin Battery """
        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date)
        )
