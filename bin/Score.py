class Score:
    def __init__(self, score_name: str, owner_name: str):
        self._score_name = score_name
        self._owner_name = owner_name
        self.__history = list[Transaction]
        self.__money = 0

    @property
    def money(self):
        return self.__money

    def withdraw_money(self, sum: float):
        if self.money >= sum:
            self.__money -= sum

    def add_money(self, sum: float):
        self.__money += sum

    def __str__(self):
        return f"The owner {self._score_name} is {self._owner_name}. He/She has {self.money}."