class OfficeEquipment:
    def __init__(self, model: str, h: float, w: float, d: float, color: bool):
        self.model = model
        self.h = h
        self.w = w
        self.d = d
        self.color = color

    def __str__(self):
        return str(self.__dict__)


class Printer(OfficeEquipment):
    def __init__(self, model: str, h: float, w: float, d: float, color: bool, pp: int):
        super().__init__(model, h, w, d, color)
        # pages printed
        self.pp = pp


class Scanner(OfficeEquipment):
    def __init__(self, model: str, h: float, w: float, d: float, color: bool, dpi: int):
        super().__init__(model, h, w, d, color)
        # dpi
        self.dpi = dpi


class Xerox(OfficeEquipment):
    def __init__(self, model: str, h: float, w: float, d: float, color: bool, ppm: int):
        super().__init__(model, h, w, d, color)
        # pages per minute
        self.ppm = ppm


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.storage = {}
        self.inventory_number = 0

    def receive(self, oe: OfficeEquipment, amount: int):
        self.inventory_number += 1
        self.storage.update({self.inventory_number: [oe, amount]})

    def show_storage(self):
        print(f'{self.name}:')
        if len(self.storage):
            for key, value in self.storage.items():
                print(f'#{key}: {value[0]} - {value[1]} pcs')
        else:
            print('!!!empty!!!')

    def transfer(self, inventory_number: int, dept: str):
        of_eq = self.storage.pop(inventory_number)
        print(f'Has transferred to {dept}: {of_eq[0]}, {of_eq[1]} pcs')


wh = Warehouse('Warehouse #1')
wh.show_storage()
p = Printer('Canon MX2140', 400, 300, 200, True, 100)
wh.receive(p, 1)
wh.show_storage()
wh.transfer(1, 'Laboratory')
wh.show_storage()