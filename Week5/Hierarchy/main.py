# Программирование на языке высокого уровня (Python).
# Задание №6. Вариант 5
#
# Выполнил: Шевченко Д.А.
# Группа: Пиж-б-о-23-2
# E-mail: 2212denis@gmail.com

from unlimited_pass import UnlimitedPass
from limited_pass import LimitedPass
from limited_trips_pass import LimitedTripsPass


def test_travel_passes():
    # Создаем объекты
    unlimited_pass = UnlimitedPass("UP123")
    limited_pass = LimitedPass("LP456", limit=5)
    limited_trips_pass = LimitedTripsPass("LTP789", trips_limit=3)

    # Используем поездки
    unlimited_pass.use_trip()  # Безлимитный билет
    limited_pass.use_trip()    # Билет с ограничением
    limited_trips_pass.use_trip()  # Билет с ограничением поездок

    # Деактивируем билет
    limited_pass.deactivate()
    limited_pass.use_trip()  # Попытка использовать деактивированный билет

    # Выводим информацию о билетах
    print(unlimited_pass)
    print(limited_pass)
    print(limited_trips_pass)


if __name__ == "__main__":
    test_travel_passes()
