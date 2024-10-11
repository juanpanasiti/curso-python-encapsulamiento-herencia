from person import Person
from student import Student
from professor import Professor

def run():
    # john_doe = Person('John', 'Doe')
    # print(john_doe)
    # print(john_doe.firstname)
    # print(john_doe.get_lastname())
    # john_doe.set_lastname('    CONDORITO  ')
    # print(john_doe.get_lastname())
    # print(john_doe._lastname)

    # print(john_doe.is_registered)

    # john_doe.email = 'john.doe@YAHOO.COM'

    # print(john_doe.is_registered)

    # Pruebas de setteo de firstname
    # print(john_doe.firstname)
    # john_doe.firstname = 'JOHN'
    # print(john_doe.firstname)



    # print(john_doe._lastname)  # Se puede, pero no deberíamos (por convensión)
    # print(john_doe._Person__email)  # Se puede, pero no deberíamos (por convensión)


    # Herencia
    # john_doe = Student('John', 'Doe', '12345')

    # john_doe._address = 'Av. Evergreen 234'
    # print(john_doe._address)

    # Herencia Multiple
    john_doe = Professor('John', 'Doe', '12345')

    john_doe._address = 'Av. Evergreen 234'
    print(john_doe.salary)
    print(john_doe._address)
    print(john_doe.title)
    pass


if __name__ == '__main__':
    run()
