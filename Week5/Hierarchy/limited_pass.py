from travel_pass import TravelPass


class LimitedPass(TravelPass):
    def __init__(self, pass_id: str, limit: int):
        super().__init__(pass_id)
        self.__limit = limit
        self.__trips_used = 0

    def use_trip(self):
        """Переопределение метода для билета с ограничением."""
        if self._is_active and self.__trips_used < self.__limit:
            self.__trips_used += 1
            print(f"""Поездка списана с билета {self._pass_id}
                  . Осталось поездок: {self.__limit - self.__trips_used}.""")
        elif not self._is_active:
            print(f"Билет {self._pass_id} неактивен.")
        else:
            print(f"Лимит поездок исчерпан для билета {self._pass_id}.")

    def __str__(self):
        return f"""LimitedPass(ID: {self._pass_id}, Active: {self._is_active}
        , Trips Used: {self.__trips_used}, Limit: {self.__limit})"""
