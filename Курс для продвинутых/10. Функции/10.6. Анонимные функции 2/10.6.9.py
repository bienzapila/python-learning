mixed_list = ['cow', 12, 'chicken', 'sand', 75]

print(max(filter(lambda x: True if type(x) == int else False, mixed_list)))