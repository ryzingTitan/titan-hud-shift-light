import configparser


class ConfigService(object):
    def __init__(self, config_file: str):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.rabbitmq_config = self.config['RabbitMQ']
        self.rpm_thresholds_config = self.config['RPM_THRESHOLDS']
        self.gpio_pins_config = self.config['GPIO_PINS']

    def get_rabbitmq_host(self) -> str:
        return self.rabbitmq_config['host']

    def get_rabbitmq_vhost(self) -> str:
        return self.rabbitmq_config['vhost']

    def get_rabbitmq_queue(self) -> str:
        return self.rabbitmq_config['queue']

    def get_first_green_lights_threshold(self) -> int:
        return int(self.rpm_thresholds_config['first_green_lights_threshold'])

    def get_second_green_lights_threshold(self) -> int:
        return int(self.rpm_thresholds_config['second_green_lights_threshold'])

    def get_first_yellow_lights_threshold(self) -> int:
        return int(self.rpm_thresholds_config['first_yellow_lights_threshold'])

    def get_second_yellow_lights_threshold(self) -> int:
        return int(self.rpm_thresholds_config['second_yellow_lights_threshold'])

    def get_red_lights_threshold(self) -> int:
        return int(self.rpm_thresholds_config['red_lights_threshold'])

    def get_left_first_green_led_pin(self) -> int:
        return int(self.gpio_pins_config['left_first_green_led_pin'])

    def get_right_first_green_led_pin(self) -> int:
        return int(self.gpio_pins_config['right_first_green_led_pin'])

    def get_left_second_green_led_pin(self) -> int:
        return int(self.gpio_pins_config['left_second_green_led_pin'])

    def get_right_second_green_led_pin(self) -> int:
        return int(self.gpio_pins_config['right_second_green_led_pin'])

    def get_left_first_yellow_led_pin(self) -> int:
        return int(self.gpio_pins_config['left_first_yellow_led_pin'])

    def get_right_first_yellow_led_pin(self) -> int:
        return int(self.gpio_pins_config['right_first_yellow_led_pin'])

    def get_left_second_yellow_led_pin(self) -> int:
        return int(self.gpio_pins_config['left_second_yellow_led_pin'])

    def get_right_second_yellow_led_pin(self) -> int:
        return int(self.gpio_pins_config['right_second_yellow_led_pin'])

    def get_left_red_led_pin(self) -> int:
        return int(self.gpio_pins_config['left_red_led_pin'])

    def get_right_red_led_pin(self) -> int:
        return int(self.gpio_pins_config['right_red_led_pin'])
