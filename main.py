from decimal import Decimal
from bin.User import User
from bin.Transaction import Transaction


if __name__ == '__main__':

    test_user = User("Artem", "Kovalenko")
    test_user.create_new_score("cash")
    test_user.create_new_score("card")
    test_tran = Transaction(test_user["cash"], test_user["card"], Decimal("28.7"), "test transaction")
    print(test_tran)
    test_tran.perform()
    print("\n", test_tran)
    # print(test_user)