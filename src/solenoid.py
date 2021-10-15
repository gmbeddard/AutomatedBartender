from abc import ABC, abstractmethod


class Solenoid(ABC):
    pin: int

    @abstractmethod
    def open(self):
        """
        opens solenoid
        :return: None
        """

    @abstractmethod
    def close(self):
        """
        closes solenoid
        :return: None
        """

    @abstractmethod
    def is_open(self) -> bool:
        """
        gets current state of this solenoid
        :return: SolenoidState
        """
