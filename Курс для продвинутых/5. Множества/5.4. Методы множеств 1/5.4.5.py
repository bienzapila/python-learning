n = int(input())
na = n
user = set()


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


cnt = 0
for _ in range(n):
    s = input().split(":")
    if s[0] not in user and s[1].lstrip() == "Correct":
        cnt += 1
        user.add(s[0])
    if s[0] in user:
        na -= 1


avrg = int_r((cnt / na) * 100)

if avrg == 0:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    print(f"Верно решили {cnt} учащихся")
    print(f"Из всех попыток {avrg}% верных")
