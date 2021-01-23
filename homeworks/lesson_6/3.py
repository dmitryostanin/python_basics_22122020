class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p1 = Position('Ivan', 'Ivanov', 'Taxi Driver', 35000, 10000)
p2 = Position('Peter', 'Petrov', 'Actor', 50000, 8000)
print(p1.get_full_name(), p1.get_total_income())
print(p2.get_full_name(), p2.get_total_income())
