first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(x)-len(y)) for x,y in zip(first,second) if len(x) != len(y))

# print(list(y for y in range(0,len(second)+1)))


second_result = (len(first[x]) == len(second[x]) for x in range(0,len(first)))


print(list(first_result))
print(list(second_result))