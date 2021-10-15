from abc import ABC, abstractmethod


class Sensor(ABC):
    pin: int

    @abstractmethod
    def get_value(self) -> float:
        """
        gets value from the sensor
        :return: None
        """