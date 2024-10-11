from person import Person


class Student(Person):
    def __init__(self, firstname, lastname, legajo):
        email = f'{firstname}.{lastname}@utn.edu.ar'
        super().__init__(firstname, lastname, email)
        self.legajo = legajo

# Reconocer el uso de herencia:
# un estudiante siempre ES una persona
# una persona no siempre ES un estudiante