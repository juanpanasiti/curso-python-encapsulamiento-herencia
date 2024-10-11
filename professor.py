from person import Person
from employee import Employee


class Professor(Person, Employee):
    def __init__(self, firstname, lastname, title='', job='', salary=0, email='', address=''):
        Person.__init__(self, firstname, lastname, email, address)
        Employee.__init__(self, job, salary)
        self.title = title
