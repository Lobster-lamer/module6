from consoleTextStyle import ConsoleTextStyle as CoTeST
import math


class Figure:
    sides_count = 0

    def __new__(cls, color: tuple[int, int, int], *sides):
        if cls.__is_valid_color(color):
            return super().__new__(cls)
        else:
            CoTeST.colorful_text("Введён некорректный цвет, фигура не создана", CoTeST.Color.RED)

    def __init__(self, color: tuple[int, int, int], *sides, filled=True):
        if len(sides) != self.sides_count:
            self.__sides = list(int(one) for one in "1" * self.sides_count)
        else:
            self.__sides = list(sides)
        self.__color: list = list(color)
        self.filled = filled

    def __len__(self):
        return sum(self.__sides)

    @staticmethod
    def __is_valid_color(_color):
        return all(map(lambda color_chanel: 0 <= color_chanel <= 255, _color))

    def get_color(self):
        return self.__color

    def print_color(self):
        print(f"Цвета объекта класса {CoTeST.Color.PURPLE}{fig.__class__.__name__}{CoTeST.REGULAR}: "
              f"{CoTeST.Color.RED}{self.__color[0]}{CoTeST.REGULAR}, "
              f"{CoTeST.Color.GREEN}{self.__color[1]}{CoTeST.REGULAR}, "
              f"{CoTeST.Color.BLUE}{self.__color[2]}{CoTeST.REGULAR}")

    def set_color(self, *color: tuple[int, int, int]):
        if self.__is_valid_color(color):
            self.__color = color
        else:
            CoTeST.colorful_text("Введён некорректный цвет", CoTeST.Color.RED)

    def __is_valid_sides(self, sides):
        return all(map(lambda side: isinstance(side, int), sides)) and \
            all(map(lambda side: side >= 0, sides)) and \
            len(sides) == len(self.__sides)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
        else:
            CoTeST.colorful_text("Введены некорректные стороны", CoTeST.Color.RED)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], *sides):
        super().__init__(color, *sides)
        self.__sides = list(sides)
        self.__color = list(color)
        self.__radius = self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple[int, int, int], *sides):
        super().__init__(color, *sides)
        self.__sides = list(sides)
        self.__color = list(color)

    def get_square(self):
        _half_perim = len(self) / 2
        return math.sqrt(_half_perim * (_half_perim - self.__sides[0]) *
                         (_half_perim - self.__sides[1]) *
                         (_half_perim - self.__sides[2]))  # S = √(p * (p - a) * (p - b) * (p - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], side: int):
        sides = list(int(_side) for _side in str(side) * self.sides_count)
        super().__init__(color, *sides)
        self.__sides = list(sides)
        self.__color = list(color)

    def get_volume(self):
        return self.__sides[0] ** 3


if __name__ == "__main__":
    # Проверка работоспособности класса Figure

    CoTeST.colorful_text("Проверка работоспособности класса Figure", CoTeST.Color.CYAN)
    fig = Figure((0, 0, 255), 1, 2)
    print(f"\n{CoTeST.ITALIC}Создан объект класса Figure{CoTeST.REGULAR}")
    fig.print_color()
    fig.set_color(255, 0, 255)
    print(f"\n{CoTeST.ITALIC}Изменён цвет{CoTeST.REGULAR}")
    fig.print_color()
    print(f"\n{CoTeST.ITALIC}Попытка задать неправильный цвет{CoTeST.REGULAR}")
    fig.set_color(310, 0, 255)
    fig.print_color()

    print(f"\n{CoTeST.ITALIC}Попытка создать фигуру с неправильно заданным цветом{CoTeST.REGULAR}")
    fig2 = Figure((-1, 25, 257), [1])
    try:
        print(isinstance(fig2))
    except TypeError:
        print(f"{CoTeST.ITALIC}Фигура действительно не создалась{CoTeST.REGULAR}")

    # Проверка работоспособности класса Circle
    CoTeST.colorful_text("\n\nПроверка работоспособности класса Circle", CoTeST.Color.CYAN)
    circ = Circle((0, 0, 255), 2)
    print(f"Стороны круга: {circ.get_sides()}")
    print(f"{CoTeST.ITALIC}Попытка поменять длину окружности на отрицательное значение:{CoTeST.REGULAR}")
    circ.set_sides(-5)
    print(f"Стороны круга: {circ.get_sides()}")
    print(f"Площадь круга: {circ.get_square()}")
    circ2 = Circle((0, 0, 255), 2, 1, 3)
    print(f"Стороны второго круга при неправильном количестве заданных сторон: {circ2.get_sides()}")

    # Проверка работоспособности класса Triangle
    CoTeST.colorful_text("\n\nПроверка работоспособности класса Triangle", CoTeST.Color.CYAN)
    tri = Triangle((255, 2, 1), 3, 4, 5)
    print(f"Стороны треугольника: {tri.get_sides()}")
    print(f"Периметр треугольника: {len(tri)}")
    print(f"Площадь треугольника: {tri.get_square()}")
    print(f"{CoTeST.ITALIC}Попытка создать треугольник с одной стороной{CoTeST.REGULAR}")
    tri2 = Triangle((0, 0, 255), 2)
    print(f"Стороны треугольника: {tri2.get_sides()}")

    # Проверка работоспособности класса Cube
    CoTeST.colorful_text("\n\nПроверка работоспособности класса Cube", CoTeST.Color.CYAN)
    cub = Cube((255, 2, 1), 3)
    print(f"Стороны куба: {cub.get_sides()}")
    print(f"Периметр куба: {len(cub)}")
    print(f"Объём куба: {cub.get_volume()}")

    # Проверка работоспособности программы с помощью кода с сайта
    CoTeST.colorful_text("\n\nПроверка работоспособности программы с помощью кода с сайта",
                         CoTeST.Color.CYAN)
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    circle1.print_color()
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    cube1.print_color()

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
