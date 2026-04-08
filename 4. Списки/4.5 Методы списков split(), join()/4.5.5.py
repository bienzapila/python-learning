s = input()

a = s.split(".")
for num in a:
    if not (0 <= int(num) <= 255):
        print("НЕТ")
        break
else:
    print("ДА")
