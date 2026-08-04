with open(input()) as file:
    text = file.read().split()
    length = max(map(len, text))
    for word in text:
        if len(word) == length:
            print(word)