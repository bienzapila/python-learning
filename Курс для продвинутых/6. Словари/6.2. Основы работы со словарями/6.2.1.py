users = [
    {"name": "Hank", "phone": "124-3818", "email": "hank@gmail.com"},
    {"name": "Petr", "phone": "555-1618", "email": "helga@mail.net"},
    {"name": "Sasha", "phone": "449-3141", "email": ""},
    {"name": "LJ", "phone": "555-2718", "email": "lj@gmail.net"},
    {
        "name": "Maria",
        "phone": "12-129-3149",
        "email": "m.shark@yandex.ru",
        "city": "Pskov",
    },
    {"name": "Fedor", "phone": "+7445-341-0545", "email": ""},
    {
        "name": "Tony",
        "phone": "242-449-3878",
        "email": "tony.ggg@mail.ru",
        "birth_year": 1111,
    },
]

ans = []
for i in range(len(users)):
    if users[i]["phone"][-1] == "8":
        ans.append(users[i]["name"])

print(*sorted(ans))
