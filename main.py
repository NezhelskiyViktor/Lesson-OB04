# Задача: Разработать простую игру, где игрок может использовать
# различные типы оружия для борьбы с монстрами. Программа должна
# быть спроектирована таким образом, чтобы легко можно было добавлять
# новые типы оружия, не изменяя существующий код бойцов или механизм боя.
from my_clases import *
from random import choice


# добавляем ещё один тип оружия - копьё
class Spear(Weapon):
    def attack(self, monster_name):
        print("вонзает копьё в ", monster_name, end=".\n")


print("На русские земли пришла беда!\n Напали:")
# создаем игровые объекты
monsters = ["Змей горыныч", "Чудище морское", "Ведьмак кровавый", "Скелет костлявый"]  # создаем список монстров
fighters = ["Илья Муромец", "Добрыня Никитич", "Алёша Попович"]  # создаем список бойцов
arsenal = [Bow(), Sword(), Spear()]  # создаем арсенал оружия

gang_of_monsters = [Monster(name) for name in monsters]  # создаем армию монстров
print("\nРусские воины вышли на бой с армой монстров.")
armi_of_fighters = [Fighter(name) for name in fighters]  # создаем армию бойцов

for fighter in armi_of_fighters:
    weapon = arsenal.pop()
    fighter.set_weapon(weapon)  # вооружаем бойца


# создаем игровой метод
def game(_fighter):
    if len(gang_of_monsters) > 0:
        monster = choice(gang_of_monsters)  # выбираем случайного монстра
        if monster.get_dead():  # если монстр убит
            gang_of_monsters.remove(monster)  # удаляем его из армии
        else:
            _fighter.get_weapon().attack(monster.name)  # боец атакует
            monster.reacts()  # монстр реагирует на атаку


print("\nИ вот бой начинается!")
while gang_of_monsters:  # пока армия монстров не пуста
    for fight in armi_of_fighters:  # все бойцы в проядке очереди
        game(fight)  # идут в бой
