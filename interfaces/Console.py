def give_signal(head: str, body):
    """method for signal processing
    @param head: signal type
    @param body: signal text or data of request"""
    match head:
        case "message": message_processing(body)
        case "request": return request_processing(body)
        case "answer": answer_processing(body)
        case _: unknown_signal_processing(head, body)

def message_processing(message: str):
    """method for processing message type signal
    @param message: message's text"""
    if message in _messages:
        _messages[message]()
    else:
        print(f"Programm give a unknown message: {message}")

def request_processing(request: str):
    """method for processing request type signal
    @param request: request's text"""
    if request in _base_requests:
        return _base_requests[request]()
    elif request in _command_buffer:
        return _command_buffer[request]
    else:
        print(f"Program give a unexpected request: {request}")
        return input("-pleas, input what returned for this request->: ")

def answer_processing(answer):
    """method for processing answer type signal
    @param answer: answer's text"""
    _command_buffer["answer"] = answer

def unknown_signal_processing(head, body):
    """method for processing unknown signal type signal
    @param head: signal type
    @param body: signal text or data of request"""
    print(f"Program gave an unknown signal {head}, with body {body}")

#methods for implement base request
def next_command():
    _command_buffer.clear()
    command = input("-input command->: ").split(" ")
    return _commands[command[0]](command[1::])

def test(*params):
    """method for BTest command"""
    _completion.change_completer(test_completion)
    return "BTest"
def test_completion():
    if "answer" in _command_buffer:
        print(_command_buffer["answer"])
    else:
        print("Not got answer from program")

    _completion.change_completer(standard_completion)

def new_user(params: list):
    """method for NUser command"""
    try:
        _command_buffer["name"] = params[0]
        _command_buffer["surname"] = params[1]
    except IndexError:
        print("You have to give a two parameters: name and surname")
        return next_command()
    return "NUser"

def standard_completion():
    """method for default completion command"""
    print("Standard Completion")
    print(f"{k}: {i}\n" for k, i in _command_buffer.items())


class _Completer:
    """Class for change completion command"""
    def __init__(self):
        self._completer = standard_completion

    def change_completer(self, completer):
        self._completer = completer

    def execute(self):
        self._completer()


_completion = _Completer()

_commands = {
    "test": test,
    "new_user": new_user,
}

_base_requests = {
    "NCommand": next_command,
}

_command_buffer: dict = {}

_messages = {
    "DONE": _completion.execute,
}