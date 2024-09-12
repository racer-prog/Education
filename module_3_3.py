

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [1,'str',True]
values_dict = {'a': 2, 'b': 'str2', 'c': True}

values_list_2 = [1, True]

#print_params()
print_params(*values_list)
print_params(**values_dict)

print_params(*values_list_2, 42)

print_params(b = 25)

print_params(c = [1,2,3])