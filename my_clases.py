from abc import ABC, abstractmethod
from random import choice


# Исходные данные:
class Fighter:  # класс `Fighter`, представляющий бойца.
    # Шаг 3: Модифицируйте класс `Fighter`
    def __init__(self, name):
        self.name = name
        self.weapon = None  # добавили параметр `weapon`, для хранения объект класса `Weapon`.
        print(f"И вот на бой выходит {self.name}.") # созданный боец заявляет о себе

# добавили метод `changeWeapon()`, который позволяет изменить оружие бойца.
    def change_weapon(self, weapon):
        self.weapon = weapon


class Monster:  # класс `Monster`, представляющий монстра.
    def attack(self):
        print("монстр " + choice(["ренен.", "падает замертво.", "отступает."]))


# Шаг 1:Создайте абстрактный класс для оружия
# Создаем абстрактный класс `Weapon`, который содержит абстрактный метод `attack()`.
class Weapon(ABC):  # абстрактный класс `Weapon`
    @abstractmethod
    def attack(self):  # абстрактный метод `attack()`
        pass


# Шаг 2: Реализуйте конкретные типы оружия
# Каждый из этих классов реализует метод `attack()` своим уникальным способом.
class Sword(Weapon):
    def attack(self):
        print("Бьет мечом и ...")


class Bow(Weapon):
    def attack(self):
        print("Стреляет из лука и ...")
