class Config:
    theme = 'light'

    def __init__(self, app_name):
        self.app_name = app_name

    def get_theme(self):
        return self.theme
