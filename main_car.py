from car import Car
from vehicle import Vehicle

def run():
    logan = Car('Renault', 'logan', 'nafta')
    logan.run()

    # vehicle = Vehicle('gasoil') # No se pude crear un objeto del tipo de una clase abstracta

if __name__ == '__main__':
    run()