class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name_new: str):
        self._name = name_new

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author_new: str) -> None:
        self._author = author_new

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        Book.__init__(self, name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages_new: int) -> None:
        if not isinstance(pages_new, int):
            raise TypeError("Вводимое значение должно быть целочисленного типа")
        if pages_new <= 0:
            raise ValueError("Вводимое значение не должно быть отрицательным")
        self._pages = pages_new

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        Book.__init__(self, name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration_new: float) -> None:
        if not isinstance(duration_new, float):
            raise TypeError("Вводимое значение должно быть числом  с плавающей точкой")
        if duration_new <= 0:
            raise ValueError("Вводимое значение не должно быть отрицательным")
        self._duration = duration_new


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
