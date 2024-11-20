
def is_prime(func):
    def wrapper(*args,**kwargs):
        num = func(*args,**kwargs)
        if num < 2:
            return "Составное"
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return "Составное"
        return "Простое"

    return wrapper

@is_prime
def sum_three(*args,**kwargs):
    summ_ = 0
    for i in args:
        # print(i)
        summ_ += int(i)
    print(summ_)
    return summ_


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)

