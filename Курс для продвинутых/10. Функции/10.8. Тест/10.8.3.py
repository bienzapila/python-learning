def concat(*args, sep=' '):
    return sep.join(map(str, args))


print(concat('hello', 'python', 'and', 'stepik'))