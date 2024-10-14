class Vehicle: #любой транспорт

    # owner = str #владелец
    # _model = str
    # __engine_power = int
    # __color = str
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner_:str, model_:str, color_:str, engine_power_:int):
        self.owner = owner_
        self._model = model_
        self.__color = color_
        self.__engine_power = engine_power_
        __COLOR_VARIANTS = self.__COLOR_VARIANTS

    def set_color(self, new_color:str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print("Владелец:", self.owner)

    def get_color(self):
        return f"Цвет: {self.__color}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_model(self):
        return f"Модель: {self._model}"

class Sedan(Vehicle): #седан, наследник Vehicle
    __PASSENGERS_LIMIT = 5

if __name__ == "__main__":
    # Текущие цвета
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()