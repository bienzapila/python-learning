class Mailbox:
    def __init__(self):
        self._owner = None

    def get_owner(self):
        return self._owner 

    def set_owner(self, new_owner):
        if isinstance(new_owner, str):
            self._owner = new_owner
        