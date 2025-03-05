class Speaker:
    """
    Класс Speaker представляет собой абстрактный класс, который определяет интерфейс для объектов, которые могут отвечать.
    """

    def __init__(self, SpeakerName="Default"):
        """
        Инициализирует объект Speaker с именем SpeakerName.
        """
        self.name = SpeakerName

    def __getanswer(self):
        """
        Метод, который должен быть реализован в подклассах.
        """
        raise NotImplementedError("You must implement this method")

    def to_answer(self):
        """
        Метод, который должен быть реализован в подклассах.
        """
        raise NotImplementedError("You must implement this method")


class Counter:
    """
    Класс Counter представляет собой счетчик, который может увеличивать значения A и B.
    """

    def __init__(self, A=0, B=0):
        """
        Инициализирует объект Counter со значениями A и B.
        """
        self.A_count = A
        self.B_count = B

    def add_A(self):
        """
        Увеличивает значение A на 1.
        """
        self.A_count += 1

    def add_B(self):
        """
        Увеличивает значение B на 1.
        """
        self.B_count += 1


class Kitty(Speaker):
    """
    Класс Kitty представляет собой кота, который может отвечать на вопросы.
    """

    def __init__(self, SpeakerName):
        """
        Инициализирует объект Kitty с именем SpeakerName.
        """
        super().__init__(SpeakerName)
        self.__counter = Counter()

    def __getanswer(self):
        """
        Возвращает ответ кота на вопрос.
        """
        if self.__counter.B_count < self.__counter.A_count:
            self.__counter.add_B()
            return "meow-meow"
        else:
            self.__counter.add_A()
            return "moore-moore"

    def number_no(self):
        """
        Возвращает количество ответов "no".
        """
        return self.__counter.B_count

    def number_yes(self):
        """
        Возвращает количество ответов "yes".
        """
        return self.__counter.A_count

    def to_answer(self):
        """
        Возвращает ответ кота на вопрос.
        """
        answer = self.__getanswer()
        return answer


tk = Kitty("MyKitty")
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(f"{tk.name} says 'yes': {tk.number_yes()} times\
and 'no': {tk.number_no()} times.")
