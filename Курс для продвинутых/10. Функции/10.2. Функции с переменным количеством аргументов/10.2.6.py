def info_kwargs(**kwargs):
    for key in sorted(list(kwargs.keys())):
        print(f'{key}: {kwargs[key]}')