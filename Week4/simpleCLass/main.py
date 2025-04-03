# Программирование на языке высокого уровня (Python).
# Задание №4. Вариант 10
#
# Выполнил: Шевченко Д.А.
# Группа: Пиж-б-о-23-2
# E-mail: 2212denis@gmail.com


from fraction import Fraction

if __name__ == "__main__":
    # Создание дробей
    frac1 = Fraction(3, 4)
    frac2 = Fraction.from_string("2/5")

    # Операции с дробями
    sum_frac = frac1 + frac2
    sub_frac = frac1 - frac2
    mul_frac = frac1 * frac2
    div_frac = frac1 / frac2

    # Вывод результатов
    print(f"Сумма: {sum_frac}")
    print(f"Разность: {sub_frac}")
    print(f"Произведение: {mul_frac}")
    print(f"Частное: {div_frac}")

    # Сохранение и загрузка
    frac1.save("frac1.json")
    loaded_frac = Fraction.load("frac1.json")
    print(f"Загруженная дробь: {loaded_frac}")

    # Дополнительные методы
    print(f"Десятичное представление: {frac1.to_float()}")
    print(f"Правильная ли дробь: {frac1.is_proper()}")
