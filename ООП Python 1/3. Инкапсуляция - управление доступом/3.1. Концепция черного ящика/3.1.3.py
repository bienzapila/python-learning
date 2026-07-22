class Secret:
    def __init__(self, secret_message):
        self._message = secret_message

    def get_message(self):
        return self._message