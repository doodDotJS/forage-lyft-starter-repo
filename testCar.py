import unittest
from datetime import date

from Car import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        x = CarFactory.create_calliope(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertTrue(x.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        x = CarFactory.create_calliope(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertFalse(x.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 35000
        last_service_mileage = 0

        x = CarFactory.create_calliope(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertTrue(x.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 20000
        last_service_mileage = 0

        x = CarFactory.create_calliope(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertFalse(x.needs_service())


if __name__ == "__main__":
    unittest.main()
