from consoleTextStyle import ConsoleTextStyle as CoTeST


class Vehicle:
    __COLOR_VARIANTS = {"red": f"{CoTeST.Color.RED}red{CoTeST.REGULAR}",
                        "yellow": f"{CoTeST.Color.YELLOW}yellow{CoTeST.REGULAR}",
                        "green": f"{CoTeST.Color.GREEN}green{CoTeST.REGULAR}",
                        "blue": f"{CoTeST.Color.BLUE}blue{CoTeST.REGULAR}",
                        "purple": f"{CoTeST.Color.PURPLE}purple{CoTeST.REGULAR}",
                        "cyan": f"{CoTeST.Color.CYAN}cyan{CoTeST.REGULAR}",
                        "darkcyan": f"{CoTeST.Color.DARKCYAN}darkcyan{CoTeST.REGULAR}"}

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = Vehicle.__COLOR_VARIANTS[color.lower()]

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f"{self.get_model()}\n"
              f"{self.get_horsepower()}\n"
              f"{self.get_color()}")

    def set_color(self, new_color: str):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            print(f"{CoTeST.Color.CYAN}Цвет изменён на {Vehicle.__COLOR_VARIANTS[new_color.lower()]}{CoTeST.REGULAR}")
            self.__color = Vehicle.__COLOR_VARIANTS[new_color.lower()]
        else:
            print(f"{CoTeST.Color.RED}Нельзя сменить цвет на {new_color}{CoTeST.REGULAR}")


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)


if __name__ == "__main__":
    # Текущие цвета __COLOR_VARIANTS = ("red", "yellow", "green", "blue", "black")
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('PURPLE')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()

