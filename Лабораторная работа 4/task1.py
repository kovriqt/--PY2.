import random

COLORS = ['dark', 'blue', 'yellow', 'purple', 'white']
COLORS_1 = ['orange', 'green', 'indigo', 'pink', 'red ']


class T_shirt:
    def __init__(self, size: int, manufacture: (int, str)):
        """
        Создан родительский класс T-shirt
        :param size: размер
        :param manufacture: производитель
        """
        self.__size = 0
        self.__manufacture = 0
        if self.__test(size) and self.__test(manufacture):
            self.__size = size
            self.__manufacture = manufacture

    @classmethod
    def __test(cls, size):
        return type(size) in (int, str)

    @property
    def get_size(self):
        """
        Создан интерфейсный метод (геттер) для возврата значения, установленного в атрибут self._size
        :return:
        """
        return self.__size

    @get_size.setter
    def get_size(self, size):
        if self.__test(size):
            self.__size = size
        else:
            raise ValueError("Передаваемые значения должны быть типов \"int\" и \"str\"")

        """
        Создан интерфейсный метод (сеттер) для установки значения атрибуту self._size
        :param new_size:
        :return:
        """

    @get_size.deleter
    def get_size(self):
        del self.__size

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
            self.__size = manufacture
        else:
            raise ValueError("Передаваемые значения должны быть типов \"int\" и \"str\"")

        """
        Создан интерфейсный метод (сеттер) для установки значения атрибуту self._manufacture
        :param new_size:
        :return:
        """

    def paint_T-shirt(self):
        """
        Метод, который устанавливает цвет футболке
        :return: Случайный цвет
        """
        random_color = random.randint(0, len(COLORS) - 1)
        return COLORS[random_color]

    def __str__(self):
        return f"размер = {self.__size}, Производитель футболки - {self.manufacture}"

    def __repr__(self):
        return f"{self.__class__}: {self.__size!r}, {self.__manufacture!r}"


class Polo_shirt(T_shirt):
    """
    Футболка поло - дочерний класс
    """

    def __init__(self, size: int, manufacture: (int, str), model: str):
        super().__init__(size, manufacture)
        self.model = model

    @property
    def model(self) -> str:
        """
        Создан геттер
        :return: Должен вернуть модель поло
        """
        return self.model

    @model.setter
    def model(self, new_model) -> None:
        self._model = new_model

    def paint_T_shirt(self):
        """
        Метод, который устанавливает цвет поло
        :return: Случайный цвет
        """
        random_color = random.randint(0, len(COLORS_1) - 1)
        return COLORS_1[random_color]

    def __str__(self):
        return f"Размер = {self.__size}, Производитель поло - {self.manufacture}, Материал - {self.material}"

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__size!r}, {self.manufacture!r}, {self.material}"


if __name__ == "__main__":
    telecaster = Polo_shirt(6, 'Fender', "Telecaster")
    print(telecaster.paint_T_shirt())
