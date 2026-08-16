from decimal import Decimal
from enum import Enum
from datetime import datetime
from bin.Score import Score


class _TransactionType(Enum):
    """Enumerate with transaction type"""
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"
    INVALID = "invalid"

class Transaction:
    """
    Class to represent transaction
    @param sender: Sender
    @param recipient: Recipient
    @param amount: Amount
    @param comment: Comment
    """
    def __init__(self,
                 sender: Score | None = None,
                 recipient: Score | None = None,
                 amount: Decimal = Decimal(0),
                 comment: str = ""):
        self._sender = sender
        self._recipient = recipient
        self._amount = amount
        self._comment = comment
        self._transaction_type = self._determine_type()
        self.__creating_date = datetime.now()
        self.__performed_date = None
        self.__performed = False

    def _determine_type(self):
        """
        Determine transaction type.
        If a sender is None -> income type.
        If a recipient is None -> expense type.
        If a sender and a recipient is here -> transfer type.
        If a sender and a recipient is None -> invalid type.
        """
        if self._sender and self._recipient:
            return _TransactionType.TRANSFER
        elif self._sender and not self._recipient:
            return _TransactionType.INCOME
        elif not self._sender and self._recipient:
            return _TransactionType.EXPENSE
        return _TransactionType.INVALID

    def _check(self) -> tuple[bool, str]:
        """
        Check if transaction is valid.
        @return tuple[bool, str] - first element is performed or not.
        Second element is the error message.
        """
        if self._transaction_type == _TransactionType.INVALID:
            return False, "Invalid transaction type. Check the sender and recipient."
        if self._sender == self._recipient:
            return False, "Sender and recipient are same."
        if self.__performed:
            return False, "Transaction is performed."

        return True, "GOOD"

    def perform(self) -> tuple[bool, str]:
        """
        Perform transaction.
        Before call a _check method
        @return tuple[bool, str] - first element is performed or not.
        Second element is the error message.
        """
        valid, message = self._check()

        if valid:
            self._sender.decrease_money(self._amount) if self._sender else None
            self._recipient.increase_money(self._amount) if self._recipient else None
            self.__performed = True
            self.__performed_date = datetime.now()
            return True, "DONE"
        return False, message

    def __str__(self) -> str:
        return (f"{self._transaction_type.value} transaction is {"performed" if self.__performed else "not performed"}"
                + f"\n    |From: {self._sender.name if self._sender else "---"}"
                + f"\n    |To: {self._recipient.name if self._recipient else "---"}"
                + f"\n    |Amount: {self._amount}"
                + f"\n    |Creation date: {self.__creating_date}"
                + f"\n    |Performed date: {self.__performed_date if self.__performed else "---"}"
                + f"\n    |Comment: {self._comment if self._comment else "---"}")