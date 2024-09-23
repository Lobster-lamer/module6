class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = "Frrr"

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        super().__init__()
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Eagle, Horse):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


if __name__ == "__main__":
    pegas = Pegasus()

    print(pegas.get_pos())
    pegas.move(10, 15)
    print(pegas.get_pos())
    pegas.move(-5, 20)
    print(pegas.get_pos())

    pegas.voice()
