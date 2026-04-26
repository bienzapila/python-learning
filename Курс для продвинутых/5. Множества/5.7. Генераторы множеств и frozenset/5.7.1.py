# :,.!?();
sentence = "Dying for the right cause is the most human thing we can do."
ans = ""
for s in sentence:
    if s.isalpha() or s == " ":
        ans += s.lower()
ans = ans.split()
print(*sorted(set(ans)))
