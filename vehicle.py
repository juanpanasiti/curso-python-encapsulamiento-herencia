from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, model: str):
        self._model: str = model

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, model: str) -> None:
        self._model = model

    @abstractmethod
    def show_info(self):
        # return f'Vehículo modelo {self.model}'
        pass
