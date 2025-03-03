class Animal:
     def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Животные"

        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self.name = name
        self.age = age


     def move(self, speed: int) -> str:
        """
        Метод, описывающий скорость движения животного

        :param speed: Скорость движения в м/ч.
        :return: Строка с описанием движения.
        """
        return f"{self.name} движется со скоростью {speed} м/ч."

     def __str__(self) -> str:
        """
        Магический метод для представления в текстовой форме

        :return: Строка с именем и возрастом животного.
        """
        return f"{self.name}, {self.age}"

     def __repr__(self) -> str:
        """
        Магический метод для внутреннего представления объекта

        :return: строка с именем и возрастом животного.
        """
        return f"Animal(name={self.name}, age={self.age})"


class Cat(Animal):

    def __init__(self, name: str, age: int, color: str):
        """
        Создание и подготовка к работе дочернего класса "Кот"

        :param name: Порода кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)
        self.color = color

    def __str__(self) -> str:
        """
        Магический метод для представления в текстовой форме

        :return: Строка с именем, возрастом и цветом кошки.
        """
        return f"{self.name}, {self.age} лет, цвет {self.color}"

    def __repr__(self) -> str:
        """
        Магический метод для внутреннего представления объекта

        :return: Строка с именем, возрастом и цветом кошки.
        """
        return f"Cat(name={self.name}, age={self.age}, color={self.color})"

    def make_sound(self) -> str:
        """
        Возвращает звук, который издает кошка.

        :return: Строка с описанием звука.
        """
        return f"{self.name} мяукнул"

if __name__ == "__main__":
    # Примеры использования классов
    cat1 = Cat(name="Рауль", age=1, color="Серый")
    print(cat1.move(100))  # Вывод: Рауль движется со скоростью 100 м/ч.
    print(cat1.make_sound())  # Вывод: Рауль мяукнул
    print(str(cat1))  # Вывод: Рауль, 1 лет, цвет Серый
    print(repr(cat1))  # Вывод: Cat(name=Рауль, age=1, color=Серый)
    pass