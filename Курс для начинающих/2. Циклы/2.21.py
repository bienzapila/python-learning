n = int(input())
while True:
    if n <= 999:
        break
    n //= 10
print(n % 10)