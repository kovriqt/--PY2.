import doctest
from typing import Union
# TODO Написать 3 класса с документацией и аннотацией типов
class bike:
    def __init__(self, brand: str, weight: Union[int, float]):
        """
        Создание объекта Мотоцикл
        :param brand: Марка Мотоцикла
        :param weight: Масса Мотоцикла
        :raise: TypeError: Если название марки Мотоцикла не принадлежить типу str
        :raise: TypeError: Если масса Мотоцикла не принадлежит типу int или float
        :raise: ValueError: Если масса Мотоцикла меньше нуля
        Пример:
        >>> auto = Auto("Honda", 2.5)
        """
        if not isinstance(brand, str):
            raise TypeError("Название марки Мотоцикла должно быть типа str")
        self.brand = brand
        if not isinstance(weight, (int, float)):
            raise TypeError("Масса Мотоцикла должна быть типа int или float")
        if weight <= 0:
            raise ValueError("Масса Мотоцикла должна быть строго больше нуля")
        self.weight = weight

    def bike_moving_forward(self, distance: Union[int, float]) -> None:
        """

        :param distance: Расстояние, которое нужно проехать
        :raise ValueError: Расстояние не может быть отрицательным

        Пример:
        >>> bike = bike("Honda", 2.5)
        >>> bike.moto_moving_forward(10)
        """
        if distance < 0:
            raise ValueError(f"Расстояние не может быть отрицательным и не может равняться {distance}")
        ...

    def left_turn(self, angle: Union[int, float]) -> None:
        """
        :param angle: Угол поворота Мотоцикла

        Пример:
        >>> bike = bike("Honda", 2.5)
        >>> bike.left_turn(-30)
        """
        ...


class Teapot:
    def __init__(self, brand: str, capacity: Union[int, float]):
        """
        Создание объекта Чайник
        :param brand: Марка чайника
        :param capacity: Вместимость чайника
        :raise: TypeError: Если название чайника не принадлежить типу str

        Пример:
        >>> teapot = Teapot("Rondell", 0.5)
        """
        if not isinstance(brand, str):
            raise TypeError("Название чайника должно быть типа str")
        self.brand = brand
        if not isinstance(capacity, (int, float)):
            raise TypeError("Вместимость чайника должна быть типа int или float")
        if capacity <= 0:
            raise ValueError("Вместимость чайника должна быть строго больше нуля")
        self.capacity = capacity

    def pour_into_thermos(self, volume: Union[int, float]) -> None:
        """
        Наливает жидкость в чайник
        :param volume: Объем, который нужно налить
        :raise ValueError: Объем не может быть отрицательным
        :raise TypeError: Объем должен быть либо int либо float
        Пример:
        >>> teapot = Teapot("Rondell", 0.5)
        >>> teapot.pour_into_teapot(0.4)
        """
        if volume < 0:
            raise ValueError(f"Объем не может быть отрицательным и не может равняться {volume}")
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть либо int либо float")
        ...

    def drop_thermos(self) -> bool:
        """
        Функция, которая проверяет, разбит чайник или нет
        :return: Разбит или нет

        Пример:
        >>> teapot = Teapot("Rondell", 0.5)
        >>> teapot.drop_teapot()
        """
        ...

class Port:
    def __init__(self, year_of_construction: int, efficiency: int):
        """
        Создание и подготовка к работе объекта Порт
        :param country: страна в которой находится порт
        :param year: год постройки
        Пример:
        >>> port = Port(2022, 90) #инициализация
        """
        if not isinstance(year_of_construction, (int)):
            raise TypeError("Год постройки должен быть типа int")
        if year_of_construction <= 0:
            raise ValueError("Год постройки должен быть больше или не равен нулю")
        self.year_of_construction = year_of_construction

        if not isinstance(efficiency, (int)):
            raise TypeError("кпд должен быть типа int")
        if efficiency <= 0:
            raise TypeError("кпд должен быть больше нуля")

    def ship_took_off(self) -> bool:
        """
        Функция которая проверяет, уплыл корабль или нет
        :return: Уплыл ли корабль
        Примеры:
        >>> port = Port(2022, 90)
        >>> port.ship_took_off()
        """
        ...
    def come_in(self) -> bool:
        """
        Функция которая проверяет, зашли ли люди на корабль
        :return: Зашли или нет
        Примеры:
        >>> port = Port(2022, 90)
        >>> port.come_in()
        """
        ...
    def financing(self, money: Union[int, float]) -> None:
        """
        Финансирование порта
        :param money: количество денег, поступившее в порт
        :raise TypeError: money должен быть int или float
        :return: Деньги
        >>> port = Port(2022, 90)
        >>> port.financing(1000000)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("money должен быть int или float")





    if __name__ == "__main__":
        # TODO работоспособность экземпляров класса проверить с помощью doctest
        doctest.testmod()
