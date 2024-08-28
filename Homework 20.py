class Horse:
    def __init__(self):
        self.x_distance = 0  # пройденный путь
        self.sound = 'Frrr'  # звук, который издает лошадь

    def run(self, dx):
        self.x_distance += dx  # увеличивает x_distance на dx


class Eagle:
    def __init__(self):
        self.y_distance = 0  # высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издает орел

    def fly(self, dy):
        self.y_distance += dy  # увеличивает y_distance на dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


pegasus = Pegasus()
pegasus.move(10, 5)  
print(pegasus.get_pos())
pegasus.voice()