def is_prime(num):
    cnt = 0
    for i in range(2, num):
        if num % i == 0:
            cnt += 1
    if cnt != 0 or num == 1:
        return False
    else:
        return True
