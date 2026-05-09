emails = {
    "gmail.com": ["johnny", "monkey-man"],
    "hotmail.com": ["chani"],
    "yandex.ru": ["petrpn", "rtgxv5dsfsd4"],
}
ans = []
for key in emails.keys():
    for value in emails[key]:
        ans.append(value + f"@{key}")

print(*sorted(ans), sep="\n")
