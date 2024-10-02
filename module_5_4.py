


class House():

    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return  object.__new__(cls)

    def __init__(self, *args):
        self.name = args[0]
        self.number_of_floors = args [1]
        self.args = args




    def __del__(self, *args):
        print(f"{self.name} снесён, но он останется в истории")





if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    del h2
    del h3

    print(House.houses_history)