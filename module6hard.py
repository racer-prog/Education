class Figure:

    sides_count = 0

    def __init__(self, *args):
        # __sides = [int] #(список сторон (целые числа))
        # __color = [str] #(список цветов в формате RGB)
        # filled = bool #(закрашенный, bool)
        self.__sides = list(args[0])
        self.__color = list(args[1])
        self.filled = args[2]

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
            print(f"def __len__:{self.__class__.__name__}")
            print(self._Circle__sides[0], type(self._Circle__sides[0]))
            print(self._Circle__radius, type(self._Circle__radius))
            print(Circle.pi, type(Circle.pi))
            print(2*Circle.pi*self._Circle__radius)
            return int(2*Circle.pi*self._Circle__radius)
        else:
            for i in self.__sides:
                perimetr += i
            return perimetr

    def set_sides(self, *new_sides): #PROVERKA
        if len(list(new_sides)) == self.sides_count:
            self.__sides = new_sides
        else:
            pass
        #print(self.__sides)

    def init_check(self):
        import itertools
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

    def __init__(self, *args):

        self.__color = args[1]
        try:
            self.__sides = list(args[0])
            print(type(self.__sides[0]))
        except:
            self.__sides = list(args)
            print(type(self.__sides))

        num_sides = self.init_check()
        print("First", self.__sides, "num_sides", num_sides)
        print(f" args:{args}, args[0]: {args[0]}")
        print("len(self.__sides)", len(self.__sides), "self.__sides", self.__sides)
        if len(list(self.__sides)) != num_sides:
            self.__sides.clear()
            for i in range(0,self.sides_count):
                self.__sides.append(1)
        self.__radius = self.__sides[0]/(2*round(self.pi,2))
        print(self.__class__.__name__,": Finish", self.__sides, "Radius:", self.__radius, "Square: ", self.get_square())

    def get_square(self):
        return self.pi*self.__radius

class Triangle(Figure):
    sides_count = 3
    def __init__(self, *args):
        self.__sides = list(args[0])
        num_sides = self.init_check()
        #print("First", self.__sides, "num_sides", num_sides)
        if len(self.__sides) != num_sides:
            self.__sides.clear()
            for i in range(0, self.sides_count):
                self.__sides.append(1)
        print(self.__class__.__name__, ": Finish", self.__sides, "Square: ", self.get_square())

    def get_square(self):
        from math import sqrt
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]
        p = 0.5*(a+b+c)
        return sqrt(p*(p-a)*(p-b)*(p-c))


if __name__ == "__main__":

    a = Circle((3),7,7)
    b = Triangle((33,44,55),77)
    print(len(a))




