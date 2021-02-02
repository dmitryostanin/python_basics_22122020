class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, model: str, h: float, w: float, d: float, color: bool):
        self.model = model
        self.h = h
        self.w = w
        self.d = d
        self.color = color


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
