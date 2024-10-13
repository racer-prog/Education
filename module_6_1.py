class Plant:
    edible = False #съедобность
    name = str

    def __init__(self, name_):
        self.name = name_


class Animal:
    alive = True #живой
    fed = False #накормленный
    name = str

    def __init__(self, name_, fed_ = False):
        self.name = name_
        self.fed = fed_

    def eat(self, food: Plant):

        if food.edible == True:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        if food.edible == False:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    edible = False

class Fruit(Plant):
    edible = True



if __name__ == "__main__":

    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

    # Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
