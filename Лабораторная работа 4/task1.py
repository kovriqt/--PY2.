import random

COLORS = ['dark', 'blue', 'yellow', 'purple', 'white']
COLORS_1 = ['orange', 'green', 'indigo', 'pink', 'red ']


class Guitars:
    def __init__(self, string: int, manufacture: (int, str)):
        """
        Создан родительский класс Guitars
        :param string: количество струн
        :param manufacture: производитель
        """
        self.__string = 0
        self.__manufacture = 0
        if self.__test(string) and self.__test(manufacture):
            self.__string = string
            self.__manufacture = manufacture

    @classmethod
    def __test(cls, string):
        return type(string) in (int, str)

    @property
    def get_string(self):
        """
        Создан интерфейсный метод (геттер) для возврата значения, установленного в атрибут self._sring
        :return:
        """
        return self.__string

    @get_string.setter
    def get_string(self, string):
        if self.__test(string):
            self.__string = string
        else:
            raise ValueError("Передаваемые значения должны быть типов \"int\" и \"str\"")

        """
        Создан интерфейсный метод (сеттер) для установки значения атрибуту self._sring
        :param new_string:
        :return:
        """

    @get_string.deleter
    def get_string(self):
        del self.__string

    @property
    def manufacture(self):
        """
        Создан интерфейсный метод (геттер) для возврата значения, установленного в атрибут self._manufacture
        :return:
        """
        return self.__manufacture

    @manufacture.setter
    def manufacture(self, manufacture):
        if self.__test(manufacture):
            self.__string = manufacture
        else:
            raise ValueError("Передаваемые значения должны быть типов \"int\" и \"str\"")

        """
        Создан интерфейсный метод (сеттер) для установки значения атрибуту self._manufacture
        :param new_string:
        :return:
        """

    def paint_guitar(self):
        """
        Метод, который устанавливает цвет гитаре
        :return: Случайный цвет
        """
        random_color = random.randint(0, len(COLORS) - 1)
        return COLORS[random_color]

    def __str__(self):
        return f"Количество струн = {self.__string}, Производитель гитары - {self.manufacture}"

    def __repr__(self):
        return f"{self.__class__}: {self.__string!r}, {self.__manufacture!r}"


class Electric_guitars(Guitars):
    """
    Электрогитары - дочерний класс
    """

    def __init__(self, string: int, manufacture: (int, str), model: str):
        super().__init__(string, manufacture)
        self.model = model

    @property
    def model(self) -> str:
        """
        Создан геттер
        :return: Должен вернуть модель электрогитары
        """
        return self.model

    @model.setter
    def model(self, new_model) -> None:
        self._model = new_model

    def paint_guitar(self):
        """
        Метод, который устанавливает цвет гитаре
        :return: Случайный цвет
        """
        random_color = random.randint(0, len(COLORS_1) - 1)
        return COLORS_1[random_color]

    def __str__(self):
        return f"Количество струн = {self.__string}, Производитель гитары - {self.manufacture}, Модель корпуса - {self.model}"

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__string!r}, {self.manufacture!r}, {self.model}"


if __name__ == "__main__":
    telecaster = Electric_guitars(6, 'Fender', "Telecaster")
    print(telecaster.paint_guitar())
