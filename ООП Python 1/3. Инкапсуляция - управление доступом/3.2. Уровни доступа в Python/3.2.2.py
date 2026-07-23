class DatabaseConnector:
    def __init__(self):
        self.is_connected = False

    def _establish_connection(self):
        self.is_connected = True

    def connect(self):
        self._establish_connection()