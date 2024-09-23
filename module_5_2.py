from module_5_1 import House
class New_house(House):
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

if __name__ == "__main__":
    h1 = New_house('ЖК Эльбрус', 10)
    h2 = New_house('ЖК Акация', 20)

    # __str__
    print(h1)
    print(h2)

    # __len__
    print(len(h1))
    print(len(h2))
