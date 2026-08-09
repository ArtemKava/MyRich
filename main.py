from interfaces import Console as interface
class App:
    def __init__(self):
        self._command = {
            "BTest": self.base_test
        }

        interface.give_signal("message", "READY")
        self._command[interface.give_signal("request", "NCommand")]()

    def base_test(self):
        interface.give_signal("answer",
                              "for now this a all information for base test")
        interface.give_signal("message", "DONE")
if __name__ == '__main__':
    print("Hello World")
    app = App()
