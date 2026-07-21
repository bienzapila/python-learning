def true_round(num):
    number = num
    while num >= 1:
        num -= 1
    
    if num >= 0.5:
        return round(number + 0.5)
    else:
        return round(number)
    
print(true_round(3.49))