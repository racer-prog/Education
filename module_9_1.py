def apply_all_func(int_list:list[int,float], *functions):

    results = {}

    for func in functions:
        a = func(int_list)
        results[func.__name__] = a

    return results

if __name__ == "__main__":
    #print(apply_all_func([1,2,4,5,6], len,sorted,tuple))

    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))