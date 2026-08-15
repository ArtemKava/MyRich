from bin.Score import Score


class User:
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self._scores: dict[str, Score] = dict()

    def create_new_score(self, score_name: str):
        self._scores[score_name] = Score(score_name)

    def transaction(self, from_name: str, to_name: str, sum: float):
        self._scores[from_name].decrease_money(sum) if from_name in self._scores else None
        self._scores[to_name].increase_money(sum) if to_name in self._scores else None


    def __str__(self):
        return (f"User {self._name} {self._surname}\n"+
                "\n".join(f"   |Score: {str(score)}" for score in self._scores.values()))