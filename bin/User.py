from bin.Score import Score
from datetime import datetime


class User:
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self._scores: dict[str, Score] = dict()

    def create_new_score(self, score_name: str):
        self._scores[score_name] = Score(score_name)

    @property
    def name(self) -> str:
        return self._name

    def __getitem__(self, key: str) -> Score:
        return self._scores[key]

    def __str__(self) -> str:
        return (f"User {self._name} {self._surname}\n"+
                "\n".join(f"   |Score: {str(score)}" for score in self._scores.values()))