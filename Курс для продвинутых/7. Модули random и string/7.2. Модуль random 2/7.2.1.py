from random import *


def generate_ip_address():
    return f"{randrange(256)}.{randrange(256)}.{randrange(256)}.{randrange(256)}"
