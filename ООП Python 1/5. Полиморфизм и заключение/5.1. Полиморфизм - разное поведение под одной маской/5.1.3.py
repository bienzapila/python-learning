class StringSource:
    def __init__(self, string):
        self.string = string

    def get_length(self):
        return len(self.string)

class ListSource:
    def __init__(self, lst):
        self.lst = lst

    def get_length(self):
        return len(self.lst)

def print_source_length(source):
    print(f'Длина источника: {source.get_length()}')