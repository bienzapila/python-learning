def print_product_list(product_list):
    hp = {
        "яблоко": "🍎",
        "хлеб": "🍞",
        "конфеты": "🍬",
        "лимон": "🍋",
        "морковь": "🥕",
        "огурец": "🥒",
        "помидор": "🍅",
        "яйцо": "🥚",
        "чеснок": "🧄",
        "авокадо": "🥑",
        "спички": "🥢",
        "соль": "🧂",
        "филе говядины": "🥩",
        "киви": "🥝",
        "лук": "🧅",
        "сыр": "🧀",
    }
    ans = {}
    for s in product_list:
        if s not in ans:
            ans[s] = 1
        else:
            ans[s] += 1

    final = {}
    for s in ans:
        if s in hp:
            final[hp[s]] = ans[s]
        else:
            final[s] = ans[s]

    for key in final.keys():
        print(f"{key}: {final[key]}")


product_list = [
    "молоко",
    "яйцо",
    "колбаса",
    "лук",
    "помидор",
    "помидор",
    "майонез",
    "хлеб",
    "лук",
    "сливочное масло",
]
print_product_list(product_list)
