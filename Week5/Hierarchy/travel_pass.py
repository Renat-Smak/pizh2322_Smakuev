class TravelPass:
    def __init__(self, pass_id: str):
        self._pass_id = pass_id
        self._is_active = True

    def use_trip(self):
        """Базовый метод для списания поездки."""
        if self._is_active:
            print(f"Поездка списана с проездного билета {self._pass_id}.")
        else:
            print(f"Проездной билет {self._pass_id} неактивен.")

    def deactivate(self):
        """Деактивирует проездной билет."""
        self._is_active = False
        print(f"Проездной билет {self._pass_id} деактивирован.")

    def __str__(self):
        return f"TravelPass(ID: {self._pass_id}, Active: {self._is_active})"
