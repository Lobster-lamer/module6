class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


if __name__ == "__main__":
    volf = Predator('Волк с Уолл-Стрит')
    dog = Mammal('Хатико')
    seven_flower = Flower('Цветик семицветик')
    orange = Fruit('Заводной апельсин')

    print(volf.name)
    print(seven_flower.name)

    print(volf.alive)
    print(dog.fed)
    volf.eat(seven_flower)
    dog.eat(orange)
    print(volf.alive)
    print(dog.fed)
