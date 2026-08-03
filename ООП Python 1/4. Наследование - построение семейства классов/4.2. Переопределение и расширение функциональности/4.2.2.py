class Logger:
    def log(self, message):
        return f'[LOG]: {message}'

class TimestampLogger(Logger):
    def log(self, message):
        super().log(message)
        return f'[LOG]: Сервер запущен (timestamp)'