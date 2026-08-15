from bin.User import User
from interfaces import Console as interface


class App:
    """A main class for the application's API.
    Interface should implement a "give_signal" method which get two parameters: type and body.
    For start program execute a "run" method.
    After executing all commands send a "DONE" message."""
    def __init__(self):
        """Initialise the application.
        Create a list with all available commands.
        On end give a "READY" signal to the interface."""
        self._users: list[User] = []
        self._command = {
            "BTest": self.base_test,
            "NUser": self.create_new_user,
        }

        interface.give_signal("message", "READY")

    def run(self):
        """Run the application."""
        self._command[interface.give_signal("request", "NCommand")]()

    #Methods implements command
    def base_test(self):
        """Method for debugging and testing purposes.
        API commands: BTest."""
        interface.give_signal("answer",
                              "\n".join(str(user) for user in self._users))
        interface.give_signal("message", "DONE")

    def create_new_user(self):
        """Method for creating a new user.
        API commands: NUser.
        during the execution sends request "name" and "surname" for the new user."""
        name = interface.give_signal("request", "name")
        surname = interface.give_signal("request", "surname")
        self._users.append(User(name, surname))
        interface.give_signal("message", "DONE")



if __name__ == '__main__':
    test_user = User("Artem", "Kovalenko")
    test_user.create_new_score("cash")
    test_user.create_new_score("card")
    print(test_user)