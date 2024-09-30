from module_5_2 import New_house

class House_(New_house):
    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) == True:
            if self.number_of_floors < other.number_of_floors:
                return True
            else:
                return False

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) <= True:
            if self.number_of_floors <= other.number_of_floors:
                return True
            else:
                return False

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) <= True:
            if self.number_of_floors > other.number_of_floors:
                return True
            else:
                return False

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) <= True:
            if self.number_of_floors >= other.number_of_floors:
                return True
            else:
                return False

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) <= True:
            if self.number_of_floors != other.number_of_floors:
                return True
            else:
                return False

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) == True:
            if self.number_of_floors == other.number_of_floors:
                return True
            else:
                return False

    def __add__(self, value):
        if isinstance(value, int) == True:
            self.number_of_floors = self.number_of_floors+value
            return self

    def __iadd__(self, value):
            return self.__add__(value)

    def __radd__(self, value):
            return self.__add__(value)


if __name__ == "__main__":
    h1 = House_('ЖК Эльбрус', 10)
    h2 = House_('ЖК Акация', 20)
    print(h1)
    print(h2)
    print(h1 == h2)  # __eq__

    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)

    h1 += 10  # __iadd__
    print(h1)

    h2 = 10 + h2  # __radd__
    print(h2)

    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__