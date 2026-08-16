from decimal import Decimal


class Score:
    """
    Class to represent a score
    """
    def __init__(self, score_name: str):
        self._score_name = score_name
        self.__money = 0

    def __str__(self):
        return f"{self._score_name} has {self.__money} money"

    def decrease_money(self, amount: Decimal):
        """
        Decrease money by amount
        :param amount:
        """
        self.__money -= amount
    def increase_money(self, amount: Decimal):
        """
        Increase money by amount
        :param amount:
        """
        self.__money += amount


    @property
    def name(self):
        return self._score_name

    @property
    def money(self):
        return self.__money