is_non_negative_num = lambda x: x.replace('.', '').isdigit() if x.count('.') < 2 else False

print(is_non_negative_num('1.05'))