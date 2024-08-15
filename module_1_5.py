immutable_var = (1,2,'str',[3,4],False)
print(immutable_var)
mutable_list = [1,2,'str',[3,4],False]
print(mutable_list)
#immutable_var[4] = mutable_list[3]
#TypeError: 'tuple' object does not support item assignment
mutable_list[4] = immutable_var[3]
print(mutable_list)
