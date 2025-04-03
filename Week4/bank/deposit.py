# Программирование на языке высокого уровня (Python).
# Задание №3. Вариант 10
#
# Выполнил: Шевченко Д.А.
# Группа: Пиж-б-о-23-2
# E-mail: 2212denis@gmail.com


class TimeDeposit:
    """Абстрактный класс - срочный вклад.

    https://ru.wikipedia.org/wiki/Срочный_вклад.

    Поля:
      - self.name (str): наименование;
      - self._interest_rate (float): процент по вкладу (0; 100];
      - self._period_limit (tuple (int, int)):
            допустимый срок вклада в месяцах [от; до);
      - self._sum_limit (tuple (float, float)):
            допустимая сумма вклада [от; до).
    Свойства:
      - self.currency (str): знак/наименование валюты.
    Методы:
      - self._check_self(initial_sum, period): проверяет соответствие данных
            ограничениям вклада;
      - self.get_profit(initial_sum, period): возвращает прибыль по вкладу;
      - self.get_sum(initial_sum, period):
            возвращает сумму по окончании вклада.
    """

    def __init__(self, name: str, interest_rate: float, 
                 period_limit: tuple[int, int], sum_limit: tuple[float, float]):
        """Инициализировать атрибуты вклада.

        Args:
            name (str): Наименование вклада
            interest_rate (float): Процентная ставка (0; 100]
            period_limit (tuple[int, int]): Допустимый срок в месяцах [от; до)
            sum_limit (tuple[float, float]): Допустимая сумма [от; до)
        """
        self.name = name
        self._interest_rate = interest_rate
        self._period_limit = period_limit
        self._sum_limit = sum_limit
        self._check_self()

    def __str__(self):
        """Вернуть строковое представление вклада.

        Returns:
            str: Форматированная строка с параметрами вклада
        """
        return (f"Наименование:       {self.name}\n"
                f"Валюта:             {self.currency}\n"
                f"Процентная ставка:  {self._interest_rate}\n"
                f"Срок (мес.):        [{self._period_limit[0]}; {self._period_limit[1]})\n"
                f"Сумма:              [{self._sum_limit[0]:,.0f}; {self._sum_limit[1]:,.0f})")

    @property
    def currency(self):
        """Получить валюту вклада.

        Returns:
            str: Статическое значение 'руб.'
        """
        return "руб."  # Не изменяется

    def _check_self(self):
        """Проверить корректность параметров вклада.

        Raises:
            AssertionError: Если параметры не проходят проверки
        """
        assert 0 < self._interest_rate <= 100, \
            "Неверно указан процент по вкладу!"
        assert 1 <= self._period_limit[0] < self._period_limit[1], \
            "Неверно указаны ограничения по сроку вклада!"
        assert 0 < self._sum_limit[0] <= self._sum_limit[1], \
            "Неверно указаны ограничения по сумме вклада!"

    def _check_user_params(self, initial_sum: float, period: int):
        """Проверить соответствие суммы и срока ограничениям вклада.

        Args:
            initial_sum (float): Проверяемая сумма
            period (int): Проверяемый срок

        Raises:
            AssertionError: Если параметры не соответствуют ограничениям
        """
        is_sum_ok = self._sum_limit[0] <= initial_sum < self._sum_limit[1]
        is_period_ok = self._period_limit[0] <= period < self._period_limit[1]
        assert is_sum_ok and is_period_ok, "Условия вклада не соблюдены!"

    def get_profit(self, initial_sum: float, period: int) -> float:
        """Рассчитать прибыль по вкладу без капитализации.

        Args:
            initial_sum (float): Первоначальная сумма
            period (int): Срок в месяцах

        Returns:
            float: Размер прибыли
        """
        self._check_user_params(initial_sum, period)
        return initial_sum * self._interest_rate / 100 * period / 12

    def get_sum(self, initial_sum: float, period: int) -> float:
        """Рассчитать итоговую сумму вклада.

        Args:
            initial_sum (float): Первоначальная сумма
            period (int): Срок в месяцах

        Returns:
            float: Сумма вклада с учетом прибыли
        """
        return initial_sum + self.get_profit(initial_sum, period)


class BonusTimeDeposit(TimeDeposit):
    """Вклад с бонусом к прибыли при выполнении условий.

    Дополнительные атрибуты:
        _bonus (dict): Параметры бонуса:
            - 'percent' (int): Процент от прибыли
            - 'sum' (float): Минимальная сумма для активации
    """

    def __init__(self, name: str, interest_rate: float,
                 period_limit: tuple[int, int], sum_limit: tuple[float, float], 
                 bonus: dict):
        """Инициализировать параметры вклада и бонуса.

        Args:
            bonus (dict): Параметры бонуса:
                - 'percent' (int): Процент от прибыли
                - 'sum' (float): Минимальная сумма
        """
        self._bonus = bonus
        super().__init__(name, interest_rate, period_limit, sum_limit)

    def __str__(self):
        """Вернуть строковое представление с информацией о бонусе.

        Returns:
            str: Форматированная строка параметров с бонусом
        """
        return (super().__str__() + "\n" +
                f"Бонус (%):          {self._bonus['percent']}\n"
                f"Бонус (мин. сумма): {self._bonus['sum']:,.0f}")

    def _check_self(self):
        """Дополнительная проверка параметров бонуса."""
        super()._check_self()
        assert isinstance(self._bonus, dict) and "percent" in self._bonus and "sum" in self._bonus, \
            "Неверно указан бонус!"

    def get_profit(self, initial_sum: float, period: int) -> float:
        """Рассчитать прибыль с учетом бонуса.

        Returns:
            float: Общая прибыль (базовая + бонусная)
        """
        profit = super().get_profit(initial_sum, period)
        if initial_sum >= self._bonus["sum"]:
            profit += profit * self._bonus["percent"] / 100
        return profit


class CompoundTimeDeposit(TimeDeposit):
    """Вклад с ежемесячной капитализацией процентов."""

    def __str__(self):
        """Вернуть строковое представление с отметкой о капитализации.

        Returns:
            str: Форматированная строка параметров с капитализацией
        """
        return super().__str__() + "\nКапитализация %   : Да"

    def get_profit(self, initial_sum: float, period: int) -> float:
        """Рассчитать прибыль с учетом капитализации процентов.

        Returns:
            float: Размер прибыли по формуле сложных процентов
        """
        self._check_user_params(initial_sum, period)
        return (initial_sum * (1 + self._interest_rate / 100 / 12) 
                ** period - initial_sum)


# ---
# Данные для инициализации вкладов
deposits_data = dict(interest_rate=5, period_limit=(6, 18),
                     sum_limit=(1000, 100000))

# Список доступных вкладов
deposits = (
    TimeDeposit("Сохраняй", interest_rate=5,
                period_limit=(6, 18),
                sum_limit=(1000, 100000)),
    BonusTimeDeposit("Бонусный 2", **deposits_data,
                     bonus=dict(percent=5, sum=2000)),
    CompoundTimeDeposit("С капитализацией", **deposits_data)
)
