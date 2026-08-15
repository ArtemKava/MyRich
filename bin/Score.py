class Score:
    def __init__(self, score_name: str):
        self._score_name = score_name
        self.__money = 0

    def __str__(self):
        return f"{self._score_name} has {self.__money} money"

    def decrease_money(self, sum: float):
        self.__money -= sum
    def increase_money(self, sum: float):
        self.__money += sum


    @property
    def name(self):
        return self._score_name

    @property
    def money(self):
        return self.__money