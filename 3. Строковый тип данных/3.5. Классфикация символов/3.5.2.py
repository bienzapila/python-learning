s = input()

if (
    s.startswith('@')
    and 5 <= len(s) <= 15
    and s[1:].isalnum()
    and s == s.lower()
):
    print('Correct')
else:
    print('Incorrect')