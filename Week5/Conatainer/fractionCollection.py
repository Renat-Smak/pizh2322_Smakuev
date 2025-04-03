import json
from typing import List
from fraction import Fraction


class FractionCollection:
    """Класс-контейнер для хранения объектов Fraction."""

    def __init__(self):
        """Инициализация контейнера."""
        self._data: List[Fraction] = []

    def __str__(self):
        """Возвращает строковое представление коллекции."""
        return f"{[str(f) for f in self._data]}"

    def __getitem__(self, index: int) -> Fraction:
        """Возвращает дробь по индексу.

        Args:
            index (int): Индекс дроби.

        Returns:
            Fraction: Дробь по указанному индексу.
        """
        return self._data[index]

    def add(self, value: Fraction) -> None:
        """Добавляет дробь в коллекцию.

        Args:
            value (Fraction): Дробь для добавления.
        """
        self._data.append(value)

    def remove(self, index: int) -> None:
        """Удаляет дробь из коллекции по индексу.

        Args:
            index (int): Индекс дроби для удаления.

        Raises:
            IndexError: Если индекс выходит за пределы коллекции.
        """
        if 0 <= index < len(self._data):
            self._data.pop(index)
        else:
            raise IndexError("Index out of range")

    def save(self, filename: str) -> None:
        """Сохраняет коллекцию в JSON-файл.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w') as file:
            json.dump([{'numerator': f.numerator, 'denominator': f.denominator}
                       for f in self._data], file)

    def load(self, filename: str) -> None:
        """Загружает коллекцию из JSON-файла.

        Args:
            filename (str): Имя файла для загрузки.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            self._data = [Fraction(f['numerator'], f['denominator'])
                          for f in data]
