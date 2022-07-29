from operator import truediv
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


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        x = CarFactory.create_glissade(
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

        x = CarFactory.create_glissade(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertFalse(x.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 60001
        last_service_mileage = 0

        x = CarFactory.create_glissade(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertTrue(x.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 40000
        last_service_mileage = 0

        x = CarFactory.create_glissade(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertFalse(x.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_on = False

        x = CarFactory.create_palindrome(
            today,
            last_service_date,
            warning_light_on
        )

        self.assertTrue(x.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = False

        x = CarFactory.create_palindrome(
            today,
            last_service_date,
            warning_light_on
        )

        self.assertFalse(x.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = True

        x = CarFactory.create_palindrome(
            today,
            last_service_date,
            warning_light_on
        )

        self.assertTrue(x.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_on = False

        x = CarFactory.create_palindrome(
            today,
            last_service_date,
            warning_light_on
        )

        self.assertFalse(x.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        x = CarFactory.create_rorschach(
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

        x = CarFactory.create_rorschach(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertFalse(x.needs_service())

    def test_engine_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 60001
        last_service_mileage = 0

        x = CarFactory.create_rorschach(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertTrue(x.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 40000
        last_service_mileage = 0

        x = CarFactory.create_rorschach(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertFalse(x.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.today()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        x = CarFactory.create_thovex(
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

        x = CarFactory.create_thovex(
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

        x = CarFactory.create_thovex(
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

        x = CarFactory.create_thovex(
            today,
            last_service_date,
            current_mileage,
            last_service_mileage
        )

        self.assertFalse(x.needs_service())


if __name__ == "__main__":
    unittest.main()
