class IncorrectVinNumber(Exception):

    def __init__(self, message:str=''):
        self.message = message

class IncorrectCarNumbers(Exception):

    def __init__(self, message:str):
        self.message = message


class Car:


    def __init__(self, model_, __vin_, __numbers_):
        self.__numbers = __numbers_
        self.model = model_
        self.__vin = __vin_
        self.__is_valid_vin(__vin_)
        self.__is_valid_numbers()


    def __is_valid_vin(self,vin_number):

        if vin_number not in range(1000000, 10000000):

            raise IncorrectVinNumber("Неверный диапазон для vin номера")

        if isinstance(vin_number, int):
            pass
        else:
            raise IncorrectVinNumber("Некорректный тип vin номера")


        return True

    def __is_valid_numbers(self):
        #print(len(self.__numbers), self.__numbers)
        if isinstance(self.__numbers, str):
            pass
        else:
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")

        if len(self.__numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")

        return True




if __name__ == "__main__":
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')
