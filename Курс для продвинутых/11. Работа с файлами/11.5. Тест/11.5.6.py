file_output = input()
file_input = input()

with open(file_input) as file:
    forb_list = file.read().rstrip('\n').split()

with open(file_output) as file:
    text = file.read()
    text_lower = text.lower()
    cord = []
    for word in forb_list:
        length = len(word)
        text_lower = text_lower.replace(word, '*' * length)
    for i in range(len(text_lower)):
        if text_lower[i] == '*':
            cord.append(i)
    new_text = ''
    for i in range(len(text)):
        if i in cord:
            new_text += '*'
        else:
            new_text += text[i]

print(new_text)





