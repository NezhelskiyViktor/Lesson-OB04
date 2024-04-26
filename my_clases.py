import random
from abc import ABC, abstractmethod
from random import choice


# Исходные данные:
class Fighter:  # класс `Fighter`, представляющий бойца.
    # Шаг 3: Модифицируйте класс `Fighter`
    def __init__(self, name):
        self.name = name
        self.__weapon = None  # добавили параметр `weapon`, для хранения объект класса `Weapon`.
        print(self.name)  # созданный боец заявляет о себе

    # добавили метод `changeWeapon()`, который позволяет изменить оружие бойца.
    def set_weapon(self, weapon):
        self.__weapon = weapon

    def get_weapon(self):
        print(self.name, end=" ")
        return self.__weapon


class Monster:  # класс `Monster`, представляющий монстра.
    def __init__(self, name="Монстр"):
        self.name = name
        self.__dead = False
        print(self.name)

    def get_dead(self):
        return self.__dead

    def reacts(self):
        self.__dead = random.randint(1, 8) == 8
        if self.__dead:
            print(f"{self.name} убит.\n Ура!!!")
        else:
            print(f"{self.name} {choice(["ренен.", "атакует.", "отступает."])}")


# Шаг 1:Создайте абстрактный класс для оружия
# Создаем абстрактный класс `Weapon`, который содержит абстрактный метод `attack()`.
class Weapon(ABC):  # абстрактный класс `Weapon`
    @abstractmethod
    def attack(self, target):  # абстрактный метод `attack()`
        pass


# Шаг 2: Реализуйте конкретные типы оружия
# Каждый из этих классов реализует метод `attack()` своим уникальным способом.
class Sword(Weapon):
    def attack(self, monster_name):
        print("бьет мечом в ", monster_name, end=".\n")


class Bow(Weapon):
    def attack(self, monster_name):
        print("стреляет из лука в ", monster_name, end=".\n")
