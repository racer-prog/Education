data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]



def calculate_structure_sum(args):
    res_list = []
    def dict_extract(dict_):
        a = []
        for dt in dict_:
            a.append(dt)
            a.append(dict_[dt])
        return a
    def first(args2):
        for i in args2:
            if isinstance(i, dict) == True:
                #print(i, dict_extract(i))
                i = dict_extract(i)
            if isinstance(i, int | str) != True:
                first(i)
            else:
                res_list.append(i)

    first(args)
    print(res_list)
    sum_all = 0
    for r in res_list:
        if isinstance(r, int) == True:
            sum_all += r
        if isinstance(r, str) == True:
            sum_all += len(r)
    return sum_all



print(calculate_structure_sum(data_structure))



