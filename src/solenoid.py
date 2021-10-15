from abc import ABC
from enum import IntEnum


class SolenoidState(IntEnum):
    OPEN = 1
    CLOSED = 0


class Solenoid(ABC):
    pin: int

    def open(self):
        """
        opens solenoid
        :return: None
        """

    def close(self):
        """
        closes solenoid
        :return: None
        """

    def get_state(self) -> SolenoidState:
        """
        gets current state of this solenoid
        :return: SolenoidState
        """
