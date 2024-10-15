class Horse:
    ''' Класс Лошадь '''

    def __init__(self, x_distance_=0, sound_="Frrr"):

        self.x_distance = x_distance_
        self.sound = sound_
        # print(f"init: {self.__doc__}, Атрибуты: {self.__dict__}")

    def run(self, dx_):
        self.x_distance += dx_

class Eagle:
    ''' Класс Орел '''

    def __init__(self, y_distance_=0, sound_="I train, eat, sleep, and repeat"):


        self.y_distance = y_distance_
        self.sound = sound_
        # print(f"init: {self.__doc__}, Атрибуты: {self.__dict__}")

    def fly(self, dy_):
        self.y_distance += dy_

class Pegasus(Horse, Eagle):
    ''' Класс Пегас '''

    def __init__(self):
        super().__init__()
        Eagle.__init__(self)
        # print(f"init: {self.__doc__}, Атрибуты: {self.__dict__}")

    def move(self, dx_, dy_):
        super().run(dx_)
        super().fly(dy_)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)



if __name__ == "__main__":

    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()