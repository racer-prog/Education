import threading, time




class Knight(threading.Thread):

    def __init__(self, name:str, power:int, counter_=100):
        # threading.Thread.__init__(self)
        super().__init__()
        self.name = name
        self.power = power
        self.counter = counter_
        self.day_count = 0

    def wars(self):

        while self.counter > 0:
            self.counter -= self.power
            self.day_count += 1
            time.sleep(1)
            print(f"{self.name} сражается {self.day_count} дней, осталось {self.counter} воинов.")


    def run(self):
        print(f"{self.name}, на нас напали!\n")
        self.wars()
        print(f"{self.name} одержал победу спустя {self.day_count} дней(дня)!")




if __name__ == "__main__":
    # Создание класса
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    # Запуск потоков и остановка текущего
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    # Вывод строки об окончании сражения