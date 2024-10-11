from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    @abstractmethod
    def run(self):
        pass