ans = {}


def bank(operation, id, amount):
    if id not in ans:
        if operation == "top up":
            ans[id] = amount
        elif operation == "show balance":
            ans[id] = 0
            print(ans[id])
    elif id in ans:
        if operation == "top up":
            ans[id] += amount
        elif operation == "withdraw" or operation == "pay":
            ans[id] -= amount
        elif operation == "show balance":
            print(ans[id])
