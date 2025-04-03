from travel_pass import TravelPass
from datetime import datetime, timedelta


class LimitedTripsPass(TravelPass):
    def __init__(self, pass_id: str, trips_limit: int,
                 reset_period_days: int = 1):
        super().__init__(pass_id)
        self.__trips_limit = trips_limit
        self.__trips_used = 0
        self.__reset_period_days = reset_period_days
        self.__last_reset_date = datetime.now()

    def use_trip(self):
        """Использование поездки с учетом периодического сброса."""
        self.__reset_if_period_passed()  # Сброс счетчика, если период истек

        if self._is_active and self.__trips_used < self.__trips_limit:
            self.__trips_used += 1
            print(f"""Поездка списана с билета {self._pass_id}. Осталось
                   поездок: {self.__trips_limit - self.__trips_used}.""")
        elif not self._is_active:
            print(f"Билет {self._pass_id} неактивен.")
        else:
            print(f"Лимит поездок исчерпан для билета {self._pass_id}.")

    def __reset_if_period_passed(self):
        """Сбрасывает счетчик поездок, если прошел период сброса."""
        now = datetime.now()
        time_since_last_reset = now - self.__last_reset_date

        if time_since_last_reset >= timedelta(days=self.__reset_period_days):
            self.__trips_used = 0
            self.__last_reset_date = now
            print(f"Счетчик поездок для билета {self._pass_id} сброшен.")

    def __str__(self):
        return f"""LimitedTripsPass(ID: {self._pass_id}, Active:
         {self._is_active}, Trips Used: {self.__trips_used},
         Limit: {self.__trips_limit}, Reset Period:
         {self.__reset_period_days} days)"""
