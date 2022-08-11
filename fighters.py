from random import randint
from typing import List


class Unit:
    damage_done = 0

    def __init__(self, name: str, health: int) -> None:
        self.health = health
        self.name = name

    def __str__(self) -> str:
        return self.name

    @property
    def damage(self) -> int:
        """Урон"""
        self.damage_done = randint(1, 4)
        return self.damage_done

    def hit(self, unit: 'Unit') -> None:
        """Удар"""
        unit.health -= self.damage


class Fighters:

    def __init__(self) -> None:
        self._fighters: List = []
        self.position = 0

    def __next__(self) -> Unit:
        if self.position >= len(self._fighters):
            self.position = 0
        fighter = self._fighters[self.position]
        if fighter.health <= 0:
            raise StopIteration()
        self.position += 1
        if self.position >= len(self._fighters):
            self.position = 0
            self._fighters.reverse()
        return fighter

    def alive(self) -> bool:
        return all([fighter.health for fighter in self._fighters])

    def add_fighter(self, fighter: Unit) -> None:
        """Добавляем бойца"""
        self._fighters.append(fighter)


def start():
    monster = Unit('Monster', 10)
    hero = Unit('Hero', 10)

    fighters = Fighters()
    fighters.add_fighter(hero)
    fighters.add_fighter(monster)

    while fighters.alive():
        f1 = next(fighters)
        f2 = next(fighters)
        f1.hit(f2)
        print(f'{f2} was damaged and lost {f1.damage_done} health and now has {f2.health} health.')


if __name__ == '__main__':
    start()
