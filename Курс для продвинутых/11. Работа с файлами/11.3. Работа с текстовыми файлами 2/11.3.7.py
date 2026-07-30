
def generate_name(name, surname):
    from random import choice
    with open(name) as name_file, open(surname) as surname_file:
        names = name_file.readlines()
        for i in range(len(names)):
            names[i] = names[i].rstrip('\n')

        surnames = surname_file.readlines()
        for i in range(len(surnames)):
            surnames[i] = surnames[i].rstrip('\n')

        return choice(names) + " " + choice(surnames)

