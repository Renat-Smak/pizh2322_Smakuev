from travel_pass import TravelPass


class UnlimitedPass(TravelPass):
    def __init__(self, pass_id: str):
        super().__init__(pass_id)
        self.__unlimited_trips = True

    def use_trip(self):
        """Переопределение метода для безлимитного билета."""
        if self._is_active:
            print(f"Поездка списана с безлимитного билета {self._pass_id}.")
        else:
            print(f"Безлимитный билет {self._pass_id} неактивен.")

    def __str__(self):
        return f"UnlimitedPass(ID: {self._pass_id}, Active: {self._is_active})"
