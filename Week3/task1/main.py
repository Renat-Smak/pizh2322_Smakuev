class Roman():
    """
    Класс для работы с римскими числами.
    """

    def __init__(self, value="I"):
        """
        Инициализация объекта класса Roman.
        :param value: римское число в виде строки (по умолчанию "I")
        """
        self.value = value

    def __add__(self, other):
        """
        Сложение двух римских чисел.
        :param other: объект класса Roman
        :return: результат сложения в виде десятичного числа
        """
        return Roman.convert(self.value) + Roman.convert(other.value)

    def __sub__(self, other):
        """
        Вычитание двух римских чисел.
        :param other: объект класса Roman
        :return: результат вычитания в виде десятичного числа
        """
        return Roman.convert(self.value) - Roman.convert(other.value)

    def __mul__(self, other):
        """
        Умножение двух римских чисел.
        :param other: объект класса Roman
        :return: результат умножения в виде десятичного числа
        """
        return Roman.convert(self.value) * Roman.convert(other.value)

    def __truediv__(self, other):
        """
        Деление двух римских чисел.
        :param other: объект класса Roman
        :return: результат деления в виде десятичного числа
        """
        return Roman.convert(self.value) / Roman.convert(other.value)

    @classmethod
    def convert(cls, value):
        """
        Конвертация римского числа в десятичное и наоборот.
        :param value: римское число в виде строки или десятичное число в виде целого числа
        :return: результат конвертации в виде десятичного числа или римского числа
        """
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        decimal_numerals = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        if isinstance(value, str):
            decimal = 0
            for i in range(len(value)):
                if i > 0 and roman_numerals[value[i]] > roman_numerals[value[i - 1]]:
                    decimal += roman_numerals[value[i]] - 2 * roman_numerals[value[i - 1]]
                else:
                    decimal += roman_numerals[value[i]]
            return decimal
        elif isinstance(value, int):
            roman = ''
            for value in sorted(decimal_numerals.keys(), reverse=True):
                while value >= value:
                    roman += decimal_numerals[value]
                    value -= value
            return roman
        else:
            return 'Неверный формат входных данных'

    @property
    def decimal(self):
        """
        Получение десятичного представления римского числа.
        :return: десятичное представление римского числа
        """
        return self.convert(self.value)


num1 = Roman("I")
num2 = Roman("V")
num3 = Roman("X")
print(num1.decimal)
print(Roman.convert("XIV"))
print(num1 + num2)
print(num2 - num1)
print(num2 * num3)
print(num3 / num2)
