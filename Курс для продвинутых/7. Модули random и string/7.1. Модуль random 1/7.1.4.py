def generate_lottery_ticket():
    import random as rnd

    ans = set()
    while len(ans) != 7:
        ans.add(rnd.randrange(1, 50))
    final = ""
    for s in sorted(ans):
        final += f"{s} "
    return final[:-1]


print(generate_lottery_ticket())
