import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=bool):
        self.__sides = [sides for i in range(self.sides_count)]  # список сторон (целые числа)
        self.__color = list(color)  # список цветов в формате RGB
        self.filled = filled  # закрашенный, bool

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return True if 0 < r < 255 and 0 < g < 255 and 0 < b < 255 else False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, list_):
        if len(list_) == self.sides_count:
            for i in list_:
                if i < 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *args):
        list_ = [*args]
        if self.__is_valid_sides(list_) is True:
            self.__sides = list_


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__radius = sides / 2 * math.pi
        self.__square = 0

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__sides = sides
        self.__height = 0
        self.__square = 0
        self.__poluperimetr = sum(sides) / 2
        self.__a = self.__sides[0]
        self.__b = self.__sides[1]
        self.__c = self.__sides[2]

    def get_square(self):
        #  Возвращает площадь треугольника используя формулу Герона
        self.__square = (self.__poluperimetr * (self.__poluperimetr - self.__a)
                         * (self.__poluperimetr - self.__b)
                         * (self.__poluperimetr - self.__c)) ** 0.5
        return self.__square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__sides = sides

    def get_volume(self):
        # объём куба
        return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
