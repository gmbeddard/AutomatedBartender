from abc import ABC
from enum import IntEnum


class GPIOState(IntEnum):
    LOW = 0
    LO = 0
    HIGH = 1
    HI = 1


class GPIO_manager(ABC):
    @staticmethod
    def set_pin(pin: int, val: GPIOState):
        """
        Sets output pin to value
        :param pin: the pin
        :param val: the value
        :return: None
        """

    @staticmethod
    def get_pin(pin: int) -> GPIOState:
        """
        Gets state of a pin
        :param pin: the pin
        :return: State HIGH or LOW
        """
