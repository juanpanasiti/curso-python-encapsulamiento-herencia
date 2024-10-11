class Person:
    def __init__(self, firstname, lastname, email = '' , address = ''):
        self.firstname = firstname  # Atributo Público
        self._lastname = lastname   # Atributo Protegido
        self.__email: str = email
        self._address = address
        # self.__role: str = role

    def set_lastname(self, value: str): # Ejemplo de setter comun
        if not value.strip():  # '   Doe   ' -> 'Doe'
            raise Exception('Valor de lastname inválido')
        self._lastname = value.strip()

    def get_lastname(self):  # Ejemplo de getter comun
        return self._lastname.title()

    @property  # Atributo calculado con property
    def is_registered(self):
        return bool(self.email)
    
    # @property  # Atributo calculado con property
    # def is_admin(self):
    #     return self.__role == 'admin'
    
    @property  # Ejemplo de getter más "pythonico"
    def email(self):
        return self.__email.lower()

    @email.setter # Ejemplo de setter más "pythonico"
    def email(self, value:str):
        if (not value.strip()) or (not '@' in value):
            raise Exception('Valor de email inválido')
        self.__email = value

    @property  
    def firstname(self):
        return self._firstname.lower().title()

    @firstname.setter 
    def firstname(self, value:str):
        if not value.strip():
            raise Exception('Valor de firstname inválido')
        self._firstname = value
