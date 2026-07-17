def product_of_odds(data):
    from functools import reduce
    
    return reduce(lambda x, y: x * y, filter(lambda x: True if x % 2 == 1 else False, data), 1)