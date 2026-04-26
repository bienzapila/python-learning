files = [
    "pygen_icon.png",
    "Oppenheimer(2024).mkv",
    "ideas.TxT",
    "codes.txt",
    "avatar.PNG",
]
ans = []
for s in files:
    if ".png" in s.lower():
        ans.append(s.lower())

print(*sorted(set(ans)))
