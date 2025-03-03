# TODO Написать 3 класса с документацией и аннотацией типов

import doctest


class Pencil:
    def __init__(self, color: str, length: int):
        """
        Создание и подготовка к работе объекта "Карандаш"

        :param color: Цвет карандаша
        :param length: Длина карандаша

        Примеры:
        >>> pencil = Pencil('red', 8)
        """
        self.color = color
        self.length = length

    def sharpening_routine(self, plan_length: int):
        """
        Заточка карандаша
        :param plan_length: плановая длина карандаша
        :raise ValueError: если длина карандаша будет меньше допустимых значений
        :return: новый карандаш

        Пример:
        >>> pencil = Pencil('red', 8)
        >>> pencil.sharpening_routine(8)
        """

        if not isinstance(plan_length, int):
            raise TypeError('Плановый вес должен быть типа int')
        if plan_length < 0:
            raise ValueError('Плановый вес должен быть неотрицательным числом')
        self.length = plan_length

    def change_pencil(self, plan_color: str):
        """
        Замена карандаша
        :param plan_color: нужный цвет карандаша
        :raise ValueError: не тот цвет
        :return: вернуть карандаш

        Пример:
        >>> pencil = Pencil('red', 8)
        >>> pencil.change_pencil('red')
        """
        if not isinstance(plan_color, str):
            raise TypeError

        self.color = plan_color


class Vase:
    def __init__(self, material: str, volume: float):
        """
        Создание и подготовка к работе объекта "Ваза"

        :param material: Материал вазы
        :param volume: Объём вазы

        Примеры:
        >>> vase = Vase('glass', 12)
        """
        self.material = material
        self.volume = volume

    def add_water(self, plan_volume: float):
        """
        Добавить воды в вазу
        :param plan_volume: нужный объём
        :raise ValueError: не тот объём
        :return: вылить ненужное

        Пример:
        >>> vase = Vase('glass', 12)
        >>> vase.add_water(12)
        """
        if not isinstance(plan_volume, float):
            raise TypeError
        if plan_volume < 0:
            raise ValueError
        self.volume = plan_volume

    def pour_water(self, plan_volume: float):
        """
        Вылить воду из вазы до нужного
        :param plan_volume: нужный объём
        :raise ValueError: не тот объём
        :return: добавить

        Пример:
        >>> vase = Vase('glass', 12)
        >>> vase.add_water(12)
        """
        if not isinstance(plan_volume, float):
            raise TypeError
        if plan_volume < 0:
            raise ValueError
        self.volume = plan_volume


class Window:
    def __init__(self, width: int, height: int):
        """
        Создание и подготовка к работе объекта "Окно"

        :param width: Ширина окна
        :param height: Высота окна

        Примеры:
        >>> window = Window(20, 10)
        """
        self.width = width
        self.height = height


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
