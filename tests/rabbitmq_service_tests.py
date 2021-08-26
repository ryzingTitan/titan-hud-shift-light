import unittest
from unittest.mock import patch, MagicMock, ANY

import pika

from shift_light import rabbitmq_service, light_control_service, shift_light_service


class MyTestCase(unittest.TestCase):
    shift_light_service_test: shift_light_service
    light_control_service_test: light_control_service
    rabbitmq_service_test: rabbitmq_service

    def setUp(self) -> None:
        self.light_control_service_test = light_control_service.LightControlService()
        self.shift_light_service_test = shift_light_service.ShiftLightService(self.light_control_service_test)
        self.rabbitmq_service_test = rabbitmq_service.RabbitmqService(self.shift_light_service_test)

    @patch('pika.BlockingConnection')
    def test_start_starts_consuming_messages(self, mock_blocking_connection):
        mock_channel = MagicMock()
        mock_blocking_connection.return_value.channel.return_value = mock_channel
        expected_connection_parameters = pika.ConnectionParameters(host='localhost', virtual_host='titan-hud')

        self.rabbitmq_service_test.start()

        mock_blocking_connection.assert_called_once_with(expected_connection_parameters)
        mock_channel.basic_consume.assert_called_with(queue='rpms', on_message_callback=ANY, auto_ack=True)
        mock_channel.start_consuming.assert_called_once()


if __name__ == '__main__':
    unittest.main()
