from decimal import Decimal

def divide(first, second=0):

    if second == 0:
        if first < 0:
            return Decimal('-Infinity')
        else:
            return Decimal('Infinity')
    else:
        return first/second



if __name__ == '__main__':
    divide(-25,0)