my_dict = {
    'Senya': 1985,
    'Efrem': 1987,
    'Klava': 1990
}
print(f'Dict: {my_dict}')
print(f'Existing value: "Klava" {my_dict['Klava']}')
print(f'Not existing value "Anton": {my_dict.get('Anton')}')
my_dict.update({
    "Anfisa":1995,
    "Igor":1972
})
print(f'my_dict: {my_dict}')
print(f'Deleted value: {my_dict.pop("Klava")}')
print(f'Modified dict:{my_dict}')

print()
my_set = {False,1,4,5,5,5,5,"s",True,False,3.5,(5,6,True)}
print(f'Set: {my_set}')
my_set.update(("New",155))
a = 5
my_set.discard(a)
print(f"Убираем из множества {a}:")
print(f'Modified set: {my_set}')