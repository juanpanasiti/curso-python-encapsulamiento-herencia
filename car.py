from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, mark, model, fuel_type):
        super().__init__(fuel_type)
        self.mark = mark
        self.model = model
        
    def run(self):
        print('*aranca el auto*')
