# Использование принцыпа откытости-закрытости в Python
"""
Задача: Разработать простую игру, где игрок может использовать
различные типы оружия для борьбы с монстрами. Программа должна
быть спроектирована таким образом, чтобы легко можно было добавлять
новые типы оружия, не изменяя существующий код бойцов или механизм боя.
"""
from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print(f"Атака мечом {self.name} с силой {self.power}")

class Gun(Weapon):
    def attack(self):
        print(f"Атака пистолетом {self.name} с силой {self.power}")

class Knife(Weapon):
    def attack(self):
        print(f"Атака ножом {self.name} с силой {self.power}")

class Player:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self):
        self.weapon.attack()

    def change_weapon(self, weapon):
        self.weapon = weapon

class Monster:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Атака монстра {self.name} с силой {self.power}")

def main():
    player = Player("Игрок", Sword("Меч", 10))
    player.attack()

    monster = Monster("Монстр", 5)
    player.change_weapon(monster)
    player.attack() # Атака монстра Монстр с силой 5

    player.change_weapon(Knife("Нож", 5))
    player.attack() # Атака ножом Нож с силой 5