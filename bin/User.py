from bin.Score import Score


class User:
    def __init__(self, name: str, surname: str):
        self._name = name
        self._surname = surname
        self._scores: list[Score] = []

    def create_new_score(self, score_name: str):
        self._scores.append(Score(score_name))

    def __str__(self):
        return (f"User {self._name} {self._surname}\n"+
                "\n".join(f"   |Score: {str(score)}" for score in self._scores))