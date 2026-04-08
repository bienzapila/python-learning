print(
    *[
        int(s) ** 2
        for s in input().split()
        if int(s) % 2 == 0 and str(int(s) ** 2)[-1] != "4"
    ]
)
