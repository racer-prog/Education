

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [1,'str',True]
values_dict = {'a': 2, 'b': 'str2', 'c': True}


#print_params()
print_params(*values_list)
print_params(**values_dict)
