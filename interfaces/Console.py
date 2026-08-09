def give_signal(head: str, body: str):
    match head:
        case "message": message_processing(body)
        case "request": return request_processing(body)
        case "answer": answer_processing(body)
        case _: pass

def message_processing(message: str):
    if message in _messages:
        _messages[message]()
    else:
        print("No such message")

def request_processing(request: str):
    if request in _base_requests:
        return _base_requests[request]()
    elif request in _command_buffer:
        return _command_buffer[request]
    else:
        print("No such command")

def answer_processing(answer):
    _command_buffer["answer"] = answer

def unknown_signal_processing():
    print("Program gave an unknown signal")

def next_command():
    _command_buffer.clear()
    command = input("-->: ").split(" ")
    return _commands[command[0]](command[1::])

def test(params: list):
    _completion.change_completer(test_completion)
    return "BTest"
def test_completion():
    if "answer" in _command_buffer:
        print(_command_buffer["answer"])
    else:
        print("Not got answer from program")

    _completion.change_completer(standard_completion)

def standard_completion():
    print("Standard Completion")
    print(f"{k}: {i}\n" for k, i in _command_buffer.items())


class _Completer:
    def __init__(self):
        self._completer = standard_completion

    def change_completer(self, completer):
        self._completer = completer

    def execute(self):
        self._completer()


_completion = _Completer()

_commands = {
    "test": test,
}

_base_requests = {
    "NCommand": next_command,
}

_command_buffer: dict = {}

_messages = {
    "DONE": _completion.execute,
}