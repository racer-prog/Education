import threading
from random import randint
# from threading import Thread, Lock
from time import sleep

class Bank(threading.Thread):

    def __init__(self, balance:int=0):
        # super().__init__()
        threading.Thread.__init__(self)
        self.balance = balance
        self.lock_ = threading.Lock()
        # print(self.lock_.locked())

    def deposit(self):
        counter = 100
        for i in range(counter):
            if self.balance >= 500 and self.lock_.locked():
                # print(f"{self.lock_.locked()} lock - СНИМАЕМ")
                self.lock_.release()
            money = randint(50,500)
            self.balance += money
            print(f"Пополнение: {money}. Баланс: {self.balance}\n")
            sleep(0.001)

    def take(self):
        counter = 100
        for i in range(counter):
            money = randint(50, 500)
            print(f"Запрос на {money}")
            if self.balance >= money :
                self.balance -= money
                print(f"Снятие: {money}. Баланс: {self.balance}\n")
            else:
                print("Запрос отклонен, недостаточно средств\n")
                self.lock_.acquire()

            sleep(0.001)


if __name__ == "__main__":
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
