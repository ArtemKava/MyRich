from Score import Score
from Transaction import Transaction

class User:
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self.__scores: list[Score] = []
        self.__history: list[Transaction] = []