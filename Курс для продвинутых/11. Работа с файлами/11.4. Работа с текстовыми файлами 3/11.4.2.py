def write_random_numbers(n):
    import random
    with open('random.txt', 'w') as file:
        for _ in range(n):
            file.write(f'{str(random.randrange(111, 778))}\n')