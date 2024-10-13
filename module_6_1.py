class Plant:
    edible = False #съедобность
    name = str

class Animal:
    alive = True #живой
    fed = False #накормленный
    name = str

    def eat(self, *food: Plant):
        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False



class Mammal(Animal):
    pass

class Predator(Animal):
    pass


class Flower(Plant):
    pass

class Fruit(Plant):
    pass



if __name__ == "__main__":
    pass