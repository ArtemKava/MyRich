class Transaction:
    def __init__(self,
                 sender: Score | bool = False,
                 recipient: Score | bool = False,
                 sum: float = 0,
                 comment: str = ""):
        self._sender = sender
        self._recipient = recipient
        self._sum = sum
        self._comment = comment

    def check(self):
        if self._sender == self._recipient:
            return "Відправник і одержувач один і той самий"

        if self._sender != False:
            if self._sender.money < self._sum:
                return "У відправника недостатньо коштів"

        return True

    def perform(self):
        if self.check():
            self._sender.withdraw_money(self._sum)