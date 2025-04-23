from typing import Optional

from vehicle import Vehicle
from insuranceable import Insuranceable

class Car(Vehicle):
    def __init__(self, model: str, engine_number: Optional[str] = '', chassis_number: Optional[str] = ''):
        # self.model: str = model  # Público
        super().__init__(model)
        self._chassis_number: str = chassis_number  # Protegido
        self.__engine_number: str = engine_number  # Privado
        self.insurance: Insuranceable = Insuranceable()

    def show_info(self):
        return f'{self.model} - #{self._chassis_number}\nMotor #{self.__engine_number}'

    # POO - getter básico
    # def get_chassis_number(self)-> str:
    #     if not self._chassis_number:
    #         print('El vehículo no tiene grabado el número de chasis')
    #     return self._chassis_number

    # def set_chassis_number(self, chassis_number:str) -> None:
    #     if not chassis_number:
    #         print('El número de chasis no puede ser vacio')
    #         return
    #     self._chassis_number = chassis_number

    @property
    def chassis_number(self) -> str:
        return self._chassis_number

    @chassis_number.setter
    def chassis_number(self, chassis_number: str) -> None:
        self._chassis_number = chassis_number

    @property
    def engine_number(self) -> str:
        return self.__engine_number

    @engine_number.setter
    def engine_number(self, engine_number: str) -> None:
        self.__engine_number = engine_number