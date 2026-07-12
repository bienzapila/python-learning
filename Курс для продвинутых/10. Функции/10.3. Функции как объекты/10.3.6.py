numbers = input()
numbers = numbers.split()

def comparator(number):
    ans = 0
    for s in number:
        ans += int(s)
    return ans

print(*sorted(numbers, key=comparator))