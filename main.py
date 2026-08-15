from bin.User import User


if __name__ == '__main__':
    test_user = User("Artem", "Kovalenko")
    test_user.create_new_score("cash")
    test_user.create_new_score("card")
    test_user.transaction("cash", "card", 28.7)
    print(test_user)