def print_something(a, b, c, *args, **kwargs):
    print(a, b, c)
    print(kwargs, type(kwargs))

print_something(1, 2, 3, 4,5,6,7,8,9, name='mohammad', age='15', family='rezayi')