from time import sleep


class Pizza:
    """
    Класс Pizza представляет собой модель пиццы с определенными характеристиками.
    """

    def __init__(self, name: str, dough: str, sauce: str, components: list, price: str):
        """
        Инициализирует объект Pizza с заданными характеристиками.

        :param name: Название пиццы.
        :param dough: Тесто пиццы.
        :param sauce: Соус пиццы.
        :param components: Компоненты пиццы.
        :param price: Цена пиццы.
        """
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.components = components
        self.price = price

    def prepare(self):
        """
        Метод prepare выводит сообщение о подготовке пиццы.
        """
        print("Подготовка пиццы")

    def cook(self):
        """
        Метод cook выводит сообщение о жарке пиццы.
        """
        print("Жарка пиццы")

    def slice(self):
        """
        Метод slice выводит сообщение о нарезке пиццы.
        """
        print("Нарезка пиццы")

    def pack(self):
        """
        Метод pack выводит сообщение об упаковке пиццы.
        """
        print("Упаковка пиццы")

    def __str__(self):
        """
        Метод __str__ возвращает строковое представление объекта Pizza.

        :return: Строковое представление объекта Pizza.
        """
        return f"Название: {self.name}\nТесто: {self.dough}\nСоус: {self.sauce}\nКомпоненты: {self.components}\nЦена: {self.price}\n"


class PizzaPepperoni(Pizza):
    """
    Класс PizzaPepperoni представляет собой подкласс класса Pizza и реализует пиццу с начинкой "Пепперони".
    """

    def __init__(self):
        """
        Инициализирует объект PizzaPepperoni с заданными характеристиками пиццы "Пепперони".
        """
        super().__init__("Пепперони", "Вкусное", "Томатный", ["колбаски пепперони", "моцарелла"], 690)


class PizzaBBQ(Pizza):
    """
    Класс PizzaBBQ представляет собой подкласс класса Pizza и реализует пиццу с начинкой "Барбекю".
    """

    def __init__(self):
        """
        Инициализирует объект PizzaBBQ с заданными характеристиками пиццы "Барбекю".
        """
        super().__init__("Барбекю", "Вкусное", "Барбекю", ["курочка", "лук", "шампиньоны", "баклажаны", "томаты", "моцарелла"], 820)


class PizzaSeafood(Pizza):
    """
    Класс PizzaSeafood представляет собой подкласс класса Pizza и реализует пиццу с начинкой "Дары моря".
    """

    def __init__(self):
        """
        Инициализирует объект PizzaSeafood с заданными характеристиками пиццы "Дары моря".
        """
        super().__init__("Дары моря", "Вкусное", "Чесночный", ["сыр фета и моцарелла", "семга", "лук", "маслины", "креветки", "мидии"], 940)


class Order:
    """
    Класс Order представляет собой модель заказа с определенными характеристиками.
    """

    def __init__(self, terminal):
        """
        Инициализирует объект Order с заданными характеристиками.

        :param terminal: Терминал, через который будет производиться оплата заказа.
        """
        self._terminal = terminal
        self._positions = []
        self._price = 0

    def __str__(self):
        """
        Метод __str__ возвращает строковое представление объекта Order.

        :return: Строковое представление объекта Order.
        """
        return f"Список позиций: {self._positions}\nСтоимость заказа: {self._price}"

    def add_pizza(self, pizza: Pizza):
        """
        Метод add_pizza добавляет пиццу в заказ и увеличивает стоимость заказа.

        :param pizza: Пицца, которую нужно добавить в заказ.
        """
        self._positions.append(pizza.name)
        self._price += pizza.price

    @property
    def price(self):
        """
        Метод price возвращает стоимость заказа.

        :return: Стоимость заказа.
        """
        return self._price

    def confirm(self):
        """
        Метод confirm подтверждает оплату заказа через терминал.
        """
        self._terminal.confirm_payment()

    def decline(self):
        """
        Метод cancel отменяет заказ и очищает корзину.
        """
        self._positions = []
        self._price = 0
        print("Корзина очищена\n")
        sleep(2)


class Terminal:
    """
    Класс Terminal представляет собой модель терминала для заказа пиццы.
    """

    def __init__(self, menu_list=None, show_menu=True):
        """
        Инициализирует объект Terminal с заданными характеристиками.

        :param menu_list: Список пицц в меню. Если не указан, используются все три вида пиццы по умолчанию.
        :param show_menu: Флаг, определяющий, нужно ли отображать меню при создании терминала.
        """
        if not menu_list:
            # Используем все три вида пиццы по умолчанию
            menu_list = [PizzaPepperoni(), PizzaBBQ(), PizzaSeafood()]
        self._menu_list = menu_list
        self._show_menu = show_menu
        self._order = None

    def display_menu(self):
        """
        Метод display_menu отображает меню пицц.
        """
        for item in self._menu_list:
            print(item)

    def create_order(self):
        """
        Метод create_order создает новый заказ.
        """
        self._order = Order(self)

    def process_user_input(self):
        """
        Метод process_user_input обрабатывает ввод пользователя для заказа пиццы.
        """
        while True:
            if self._order is None:
                self.create_order()

            command = input("Введите номер пиццы или 'x' для выхода или 'c' для очистки корзины: ")
            if command == 'x':
                break
            elif command == 'c':
                self._order.decline()
                self.display_menu()
            else:
                try:
                    index = int(command) - 1
                    if 0 <= index < len(self._menu_list):
                        pizza = self._menu_list[index]
                        self._order.add_pizza(pizza)
                        print(f"Добавлена пицца {pizza.name}")
                except ValueError:
                    print("Неверный ввод. Попробуйте еще раз.")

    def confirm_payment(self):
        """
        Метод confirm_payment подтверждает оплату заказа.
        """
        total_price = self._order.price
        answer = input(
            f"Ваш заказ на сумму {total_price}. Желаете продолжить? y/n: ")
        if answer.lower() == 'y':
            print("Оплатите заказ!")
            return True
        else:
            self._order = None
            return False

    def accept_payment(self):
        """
        Метод accept_payment принимает оплату заказа.

        :return: True, если оплата принята.
        """
        user_input = ""
        while user_input != "+":
            print("Введите + когда закончите оплату")
            user_input = input()
        print("Оплата принята. Заказ передан в исполнение.")
        return True

    def close_order(self):
        """
        Метод close_order закрывает заказ и создает новый заказ.
        """
        if self._order is not None:
            self._order.decline()
            self._order = None
            self.create_order()

    def run(self):
        """
        Метод run запускает терминал и обрабатывает заказы.
        """
        while True:
            if self._show_menu:
                self.display_menu()
            self.process_user_input()
            if self.confirm_payment():
                self.accept_payment()
            self.close_order()


terminal = Terminal()
terminal.run()
