# Программирование на языке высокого уровня (Python).
# Задание №5. Вариант 25
#
# Выполнил: Шевченко Д.А.
# Группа: Пиж-б-о-23-2
# E-mail: 2212denis@gmail.com
from fractionCollection import FractionCollection, Fraction


if __name__ == "__main__":
    # Пример использования
    fc = FractionCollection()
    fc.add(Fraction(1, 2))
    fc.add(Fraction(3, 4))
    print(fc)

    fc.save("fractions.json")
    fc.load("fractions.json")
    print(fc)

    print(fc[0])
    fc.remove(0)
    print(fc)
