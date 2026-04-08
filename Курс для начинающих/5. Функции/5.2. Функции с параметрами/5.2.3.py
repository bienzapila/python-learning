def print_digit_sum(num):
    sum = 0
    for i in range(len(str(num))):
        sum += int(str(num)[i])
    print(sum)
