favorite_numbers = {
    "scarlett": 41,
    "den": 22,
    "viktor": 321,
    "lera": 777,
    "mahad": 4,
    "manny": 4,
    "ken": 8423,
    "borya": 12,
}
ans = {
    c: favorite_numbers[c]
    for c in favorite_numbers
    if len(str(favorite_numbers[c])) == 2
}
print(ans)
