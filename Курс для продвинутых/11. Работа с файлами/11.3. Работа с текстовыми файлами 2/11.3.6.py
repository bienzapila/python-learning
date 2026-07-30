with open(input()) as file:
    lines = file.readlines()
    count_lines = len(lines)

    count_words = 0
    for i in range(count_lines):
        lines[i] = lines[i].rstrip('\n')
        count_words += len(lines[i].split())

    count_letters = 0
    for symb in ' '.join(lines):
        if symb.isalpha():
            count_letters += 1

    print(f'''
Input file contains:
{count_letters} letters
{count_words} words
{count_lines} lines
''')
    

