from abc import ABC, abstractmethod
from datetime import date
from logging import exception


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
            year=self.last_service_date.year + 3)
        return date_of_expiry < self.current_date


class NubbinBattery(BatteryBaseClass):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date: date = last_service_date
        self.current_date: date = current_date

    def needs_service(self) -> bool:
        date_of_expiry = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        return date_of_expiry < self.current_date


class TireBaseClass(ABC):
    @abstractmethod
    def needs_service() -> bool:
        pass


class CarriganTires(TireBaseClass):
    def __init__(self, wear_indicators) -> None:
        self.wear_indicators = wear_indicators

    def needs_service(self) -> bool:
        tire_worn = False

        for x in self.wear_indicators:
            if x >= 0.9:
                tire_worn = True

        return tire_worn


class OctaprimeTires(TireBaseClass):
    def __init__(self, wear_indicators) -> None:
        self.wear_indicators = wear_indicators

    def needs_service(self) -> bool:
        tire_worn = False

        sum = 0
        for x in self.wear_indicators:
            sum = sum + x

        if sum >= 3:
            tire_worn = True

        return tire_worn


class Car():
    def __init__(self, Engine: EngineBaseClass, Battery: BatteryBaseClass, Tires: TireBaseClass):
        self.engine: EngineBaseClass = Engine
        self.battery: BatteryBaseClass = Battery
        self.tires: TireBaseClass = Tires

    def needs_service(self) -> bool:
        toReturn = False
        engine_needs_service = self.engine.needs_service()
        if engine_needs_service:
            toReturn = True

        battery_needs_service = self.battery.needs_service()
        if battery_needs_service:
            toReturn = True

        tires_needs_service = self.tires.needs_service()
        if tires_needs_service:
            toReturn = True

        return toReturn


class CarFactory():
    tire_types = {
        "carrigan": CarriganTires,
        "octaprime": OctaprimeTires
    }

    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_type: str, tire_wear: list) -> Car:
        """ Create a Calliope with a Capulet Engine and Spindler Battery
            Valid tire types: carrigan, octaprime.
        """
        if tire_type not in self.tire_types:
            raise Exception(
                "Invalid tire type! Only 'carrigan' and 'octaprime' are valid tire types.")

        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date),
            self.tire_types[tire_type](tire_wear)
        )

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_type: str, tire_wear: list) -> Car:
        """ Create a Glissade with a Willoughby Engine and Spindler Battery
            Valid tire types: carrigan, octaprime.
        """
        if tire_type not in self.tire_types:
            raise Exception(
                "Invalid tire type! Only 'carrigan' and 'octaprime' are valid tire types.")

        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date),
            self.tire_types[tire_type](tire_wear)
        )

    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool, tire_type: str, tire_wear: list) -> Car:
        """ Create a Palindrome with a Sternman Engine and Spindler Battery
            Valid tire types: carrigan, octaprime.
        """
        if tire_type not in self.tire_types:
            raise Exception(
                "Invalid tire type! Only 'carrigan' and 'octaprime' are valid tire types.")

        return Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(last_service_date, current_date),
            self.tire_types[tire_type](tire_wear)
        )

    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_type: str, tire_wear: list) -> Car:
        """ Create a Rorschach with a Willoughby Engine and Nubbin Battery
            Valid tire types: carrigan, octaprime.
        """

        if tire_type not in self.tire_types:
            raise Exception(
                "Invalid tire type! Only 'carrigan' and 'octaprime' are valid tire types.")

        return Car(
            WilloughbyEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date),
            self.tire_types[tire_type](tire_wear)
        )

    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_type: str, tire_wear: list) -> Car:
        """ Create a Thovex with a Capulet engine and Nubbin Battery
            Valid tire types: carrigan, octaprime.
        """
        if tire_type not in self.tire_types:
            raise Exception(
                "Invalid tire type! Only 'carrigan' and 'octaprime' are valid tire types.")

        return Car(
            CapuletEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date),
            self.tire_types[tire_type](tire_wear)
        )
