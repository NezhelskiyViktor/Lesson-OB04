# Задача: Разработать простую игру, где игрок может использовать
# различные типы оружия для борьбы с монстрами. Программа должна
# быть спроектирована таким образом, чтобы легко можно было добавлять
# новые типы оружия, не изменяя существующий код бойцов или механизм боя.
from my_clases import *
from random import choice


# добавляем ещё один тип оружия - копьё
class Spear(Weapon):
    def attack(self):
        print("Вонзает копьё и ...")


# создаем игровые объекты
monster = Monster()
fighters = ["Илья Муромец", "Добрыня Никитич", "Алёша Попович"] # создаем список бойцов
arsenal = [Bow(), Sword(), Spear()]  # создаем арсенал оружия


# создаем игровой метод
def game(fighter_name):
    new_fighter = Fighter(fighter_name)  # создаем объект бойца идущего в бой
    weapon = choice(arsenal)  # выбираем ему оружие
    new_fighter.change_weapon(weapon)  # вооружаем бойца
    new_fighter.weapon.attack()  # боец атакует
    monster.attack()  # монстр реагирует на атаку


for fighter in fighters:  # в порядке очереди
    game(fighter)  # бойцы идут в бой
