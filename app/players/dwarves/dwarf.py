from app.players.player import Player
from abc import ABC, abstractmethod


class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    @abstractmethod
    def player_info(self):
        pass

    @abstractmethod
    def get_rating(self):
        pass

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")
