def divide(first, second=0):

    if second == 0:
        return "Ошибка"
    else:
        return first/second

if __name__ == '__main__':
    divide(5,0)