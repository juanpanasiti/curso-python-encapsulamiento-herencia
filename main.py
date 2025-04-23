from car import Car
from vehicle import Vehicle
from boat import Boat

def main():
    logan = Car('Renault Logan', 'XYZ987' , 'ABC123')
    # some_vehicle = Vehicle('Algo')  # Como Vehicle es una clase abstracta, no puedo crear un objeto de este tipo
    # boat = Boat() # Mismo caso de vehicle porque hereda de la clase pero no implementa 'show_info()'
    # logan = Car('Renaul Logan')
    print(logan.show_info())
    # print(f'Modelo: {logan.model}')
    # print(f'Chasis: {logan.chassis_number}')
    # print(f'Motor: {logan.engine_number}')
    # logan.chassis_number = 'DEF345'
    # logan.engine_number = '987QWE'
    # print(f'Chasis (nuevo): {logan.chassis_number}')
    # print(f'Motor (nuevo): {logan.engine_number}')
    # logan.insurance.policy_number = 'SN00001'
    # print(f'Seguro: {logan.insurance.policy_number}')

if __name__ == '__main__':
    main()
