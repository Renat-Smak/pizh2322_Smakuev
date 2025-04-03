import json
import math


class Fraction:
    """Класс для работы с обыкновенными дробями."""

    def __init__(self, numerator: int, denominator: int):
        """Инициализация дроби.

        Args:
            numerator (int): Числитель дроби.
            denominator (int): Знаменатель дроби.
        """
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __str__(self):
        """Возвращает строковое представление дроби."""
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Сложение двух дробей."""
        new_numerator = self.numerator * other.denominator
        + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Вычитание двух дробей."""
        new_numerator = self.numerator * other.denominator
        - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """Умножение двух дробей."""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """Деление двух дробей."""
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def simplify(self):
        """Упрощение дроби."""
        common_divisor = math.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    @classmethod
    def from_string(cls, str_value: str):
        """Создает объект Fraction из строки.

        Args:
            str_value (str): Строка в формате "числитель/знаменатель".
        """
        numerator, denominator = map(int, str_value.split('/'))
        return cls(numerator, denominator)

    def save(self, filename: str):
        """Сохраняет дробь в JSON-файл.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w') as file:
            json.dump({'numerator': self.numerator,
                       'denominator': self.denominator}, file)

    @classmethod
    def load(cls, filename: str):
        """Загружает дробь из JSON-файла.

        Args:
            filename (str): Имя файла для загрузки.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            return cls(data['numerator'], data['denominator'])

    def to_float(self):
        """Возвращает десятичное представление дроби."""
        return self.numerator / self.denominator

    def is_proper(self):
        """Проверяет, является ли дробь правильной."""
        return abs(self.numerator) < abs(self.denominator)
