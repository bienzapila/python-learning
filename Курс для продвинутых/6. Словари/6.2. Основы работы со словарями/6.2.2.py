users = [
    {"name": "Andrew", "email": "and@gmail.com"},
    {"name": "Tim", "phone": "555-1618", "email": "tim-tim@yandex.ru"},
    {"name": "Olivia", "phone": "449-3141", "email": ""},
    {"name": "Vika", "phone": "547-2123", "email": "Viko4ka@gmail.com"},
    {"name": "Kate", "surname": "Maltseva", "city": "Vologda"},
]

ans = []
for i in range(len(users)):
    if "email" not in users[i] or users[i]["email"] == "":
        ans.append(users[i]["name"])

print(*sorted(ans))
