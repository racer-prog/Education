class Figure:

    sides_count = 0

    def __init__(self, __color_:tuple, *args):
        # __sides = [int] #(список сторон (целые числа))
        # __color = [str] #(список цветов в формате RGB)
        filled = bool #(закрашенный, bool)
        # print(__class__,  "__init__: __color:", __color_)
        # print(__class__,  "__init__: args:", args)
        # print(__class__,  "__init__: *args:", *args)
        # print(type(args))

        if type(args) == "<class 'list'>":
            self.__sides = args
        else:
            self.__sides = list(args)
        self.__color = list(__color_)
        #self.filled = args[2]

    def get_color(self): #worked
        return self.__color

    def __is_valid_color(self, r_, g_, b_): #worked
        # print([r_,g_,b_])
        # print('range:',all(i in range(0, 256) for i in (r_, g_, b_)))
        # print('int:', all(type(i) == int for i in (r_, g_, b_)))
        if all(i in range(0, 256) for i in (r_, g_, b_)) and all(type(i) == int for i in (r_, g_, b_)) == True:
            return True
        else:
            return  False

    def set_color(self, r_, g_, b_): #worked
        if self.__is_valid_color(r_, g_, b_) == True:
            self.__color = [r_, g_, b_]
        else:
            pass

    def __is_valid_sides(self, *sides_): #worked
        #print(list(sides_))
        if all(type(i) == int for i in list(sides_)) and len(self.__sides) == len(list(sides_)):
            return True
        else:
            return False

    def get_sides(self): #worked
        return self.__sides

    def __len__(self): #worked
        perimetr = 0
        if self.__class__.__name__ == "Circle":
            # print(f"def __len__:{self.__class__.__name__}")
            # print(self._Circle__sides[0], type(self._Circle__sides[0]))
            # print(self._Circle__radius, type(self._Circle__radius))
            # print(Circle.pi, type(Circle.pi))
            # print(2*Circle.pi*self._Circle__radius)
            #return int(2*Circle.pi*self._Circle__radius)
            try:
                return self.__sides[0]
            except:
                return self.__sides
        else:
            for i in self.__sides:
                perimetr += i
            return perimetr

    def set_sides(self, *new_sides):#PROVERKA
        new_sides = list(new_sides)
        # print(self.__dict__)
        # print("NEW SIDES:", new_sides)
        # print("self.sides_count:", self.sides_count)
        # print("len(new_sides: ", len(new_sides))
        if len(new_sides) == self.sides_count:
            self.__sides = new_sides
        else:
            pass
        # print("New self.__sides:", self.__sides)

    def init_check(self):

        class_name = self.__class__.__name__
        if class_name == "Circle":
            return 1
        elif class_name == "Triangle":
            return 3
        elif class_name == "Cube":
            return 12


class Circle(Figure):
    from math import pi
    sides_count = 1

    # def __init__(self, __color_:tuple, *args):
    def __init__(self, __color_:tuple, *args):
        #super().__init__(__color_, *args)
        #print(self.__dict__)
        # self.__color = __color_
        try:
            self.__sides = list(args[0])
            #print(type(self.__sides[0]))
        except:
            self.__sides = list(args)
            #print(type(self.__sides))

        num_sides = self.init_check()
        # print(self.__class__.__name__, ": First", self.__sides, "num_sides", num_sides, "передано сторон:", len(args))
        # print(f" args:{args}, args[0]: {args[0]}")
        # print("len(self.__sides)", len(self.__sides), "self.__sides", self.__sides)
        if len(list(self.__sides)) != num_sides:
            # print("Переопределяем сторона на '1'")
            self.__sides.clear()
            for i in range(0,self.sides_count):
                self.__sides.append(1)
        self.__radius = self.__sides[0]/(2*round(self.pi,2))
        # print(self.__class__.__name__,": Finish", self.__sides, "Radius:", self.__radius, "Square: ", self.get_square())
        print()

    def get_square(self):
        return self.pi*self.__radius

class Triangle(Figure):
    sides_count = 3
    def __init__(self, __color_, *args):
        self.__color = __color_
        try:
            self.__sides = list(args[0])
        except:
            self.__sides = list(args)
        num_sides = self.init_check()
        print(self.__class__.__name__, ": First", self.__sides, "num_sides", num_sides, "передано сторон:", len(args))
        #print("First", self.__sides, "num_sides", num_sides)
        if len(self.__sides) != num_sides:
            self.__sides.clear()
            for i in range(0, self.sides_count):
                self.__sides.append(1)
        print(self.__class__.__name__, ": Finish", self.__sides, "Square: ", self.get_square())
        print()

    def get_square(self):
        from math import sqrt
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]
        p = 0.5*(a+b+c)
        if (p-a) < 0 or (p-b) < 0 or (p-c) < 0:
            pass
        else:
            return sqrt(p*(p-a)*(p-b)*(p-c))

class Cube(Figure):

    sides_count = 12

    def __init__(self, __color_:tuple, *args):
        __sides = []
        for i in range(0,self.init_check()):
            try:
                __sides.append(args[0])
            except:
                __sides.append(1)
        super(Cube,self).__init__(__color_, *__sides)
        self.__color = __color_
        self.__sides = __sides



        #print(self.__sides)

    def get_volume(self):

        return self.__sides[0]**3

if __name__ == "__main__":

    # a = Circle((3,3,3),7,5)
    # b = Triangle((33,44,55),7,4,5)
    #
    # print()


    #print(len(a))

    #c = Figure((3,3,3,),4,5,6,7)

    #d = Figure((2,2,2),3)

    # e = Cube((1,1,1),3)
    # print(e.get_volume())

    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())


