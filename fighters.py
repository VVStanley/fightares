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
        self.damage_done = randint(1, 5)
        return self.damage_done

    def hit(self, unit: 'Unit') -> None:
        """Удар"""
        unit.health -= self.damage

    def winner(self) -> str:
        """Возвращаем итоговую надпись"""
        return f"{self} Winner!!" if self.health > 0 else f"{self} Lose"


class Fighters:

    def __init__(self) -> None:
        self._fighters: List = []
        self.position = 0

    def __next__(self) -> Unit:
        if self.position >= len(self._fighters):
            self.position = 0
        fighter = self._fighters[self.position]
        self.position += 1
        if self.position >= len(self._fighters):
            self.position = 0
            self._fighters.reverse()
        return fighter

    def alive(self) -> bool:
        return all(
            [
                True if fighter.health > 0 else False
                for fighter in self._fighters
            ]
        )

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
        attacking_fighter = next(fighters)
        protection_fighter = next(fighters)
        attacking_fighter.hit(protection_fighter)
        print(
            f"{protection_fighter} was damaged and lost "
            f"{attacking_fighter.damage_done} health and "
            f"now has {protection_fighter.health} health."
        )

    print(hero.winner())
    print(monster.winner())


if __name__ == '__main__':
    start()
