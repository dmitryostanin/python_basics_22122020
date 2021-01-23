class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки: ручка')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки: карандаш')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки: маркер')


s1 = Pen('ручка')
s1.draw()
s2 = Pencil('карандаш')
s2.draw()
s3 = Handle('маркер')
s3.draw()
