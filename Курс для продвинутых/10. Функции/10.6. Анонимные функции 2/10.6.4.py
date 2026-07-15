is_num = lambda x: (x + '5').replace('.', '')[1:].isdigit() if x.count('.') < 2 and x.count('-') < 2 else False

print(is_num('--3.45'))