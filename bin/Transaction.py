from decimal import Decimal
from enum import Enum
from bin.Score import Score


class _TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"
    INVALID = "invalid"

class Transaction:
    def __init__(self,
                 sender: Score | None = None,
                 recipient: Score | None = None,
                 amount: Decimal = Decimal(0)):
        self._sender = sender
        self._recipient = recipient
        self._amount = amount
        self.__performed = False

    def _determine_type(self):
        if self._sender and self._recipient:
            return _TransactionType.TRANSFER
        elif self._sender and not self._recipient:
            return _TransactionType.INCOME
        elif not self._sender and self._recipient:
            return _TransactionType.EXPENSE
        return _TransactionType.INVALID

    def _check(self) -> tuple[bool, str]:
        type = self._determine_type()
        if type == _TransactionType.INVALID:
            return False, "неможливий тип транзакції. Перевірте відправника і одержувача"
        if self._sender == self._recipient:
            return False, "Відправник і одержувач один і той самий"
        if self.__performed:
            return False, "Транзакція вже виконана"

        return True, "GOOD"

    def perform(self) -> tuple[bool, str]:
        valid, message = self._check()

        if valid:
            self._sender.decrease_money(self._amount) if self._sender else None
            self._recipient.increase_money(self._amount) if self._recipient else None
            self.__performed = True
            return True, "DONE"
        return False, message