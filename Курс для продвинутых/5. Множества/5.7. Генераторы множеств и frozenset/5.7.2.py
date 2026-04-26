sentence = "Dying for the right cause is the most human thing we can do."
ans = ""
for s in sentence:
    if s.isalpha() or s == " ":
        ans += s.lower()

ans = ans.split()
ans = {s for s in ans if len(s) < 4}
print(*sorted(ans))
