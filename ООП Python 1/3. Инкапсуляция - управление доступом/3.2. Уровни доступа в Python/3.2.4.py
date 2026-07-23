class Component:
    def __init__(self, name, version, id):
        self.name = name
        self._id = id
        self.__version = version