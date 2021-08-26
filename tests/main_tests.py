import unittest
from unittest.mock import MagicMock

from shift_light import rabbitmq_service, shift_light_service, light_control_service, main


class MyTestCase(unittest.TestCase):
    shift_light_service_test: shift_light_service
    light_control_service_test: light_control_service
    rabbitmq_service_test: rabbitmq_service

    def setUp(self) -> None:
        self.light_control_service_test = light_control_service.LightControlService()
        self.shift_light_service_test = shift_light_service.ShiftLightService(self.light_control_service_test)
        self.rabbitmq_service_test = rabbitmq_service.RabbitmqService(self.shift_light_service_test)
        self.rabbitmq_service_test.start = MagicMock()

    def test_main_starts_rabbitmq_service(self):
        main.main(self.rabbitmq_service_test)

        self.rabbitmq_service_test.start.assert_called_once()


if __name__ == '__main__':
    unittest.main()
