class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor):
                print(i)

if __name__ == "__main__":
    my_house = House("IT_PARK",17)
    guest_house = House("Park_for_you", 5)
    my_house.go_to(17)
    guest_house.go_to(7)
