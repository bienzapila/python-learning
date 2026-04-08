s = input().lower()
a = s.split()
total = 0

total += a.count("a")
total += a.count("the")
total += a.count("an")

print(f"Общее количество артиклей: {total}")
