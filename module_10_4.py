import threading
from time import sleep
from random import randint
from queue import Queue

class Table:

    def __init__(self, number:int, guest=None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        delay = randint(3,10)
        sleep(delay)

class Cafe:

    def __init__(self,*args:Table):
        #print(args)
        self.tables = args
        self.que = Queue()

    def is_table_empty(self, table:Table):
        if table.guest is None:
            # print("Стол", table.number,"свободен")
            return True
        if table.guest != None:
            # print(table.number, "занят")
            return False

    def guest_arrival(self, *guests: Guest):
        # print([t.__dict__ for t in self.tables])
        count=0
        list_guests = list(guests)
        list_tables = list(self.tables)
        # print("Количество гостей:", len(list_guests))
        # print("Количество столов:", len(list_tables))
        count_table = 1
        for id_guest in range(1, len(list_guests)+1):
            if count_table < len(list_tables)+1 and self.is_table_empty(list_tables[count_table-1]) :
                for id_table in range(1,len(list_tables)+1):

                    # print(t.__dict__, self.is_table_empty(t))
                    # print('счетчик гостей:',id_guest,':',list_guests[id_guest-1].name)
                    # print("счетчик перебора столов:", count_table)
                    # print(self.is_table_empty(list_tables[count_table-1]))
                    self.tables[count_table-1].guest = list_guests[id_guest-1]
                    th = Guest(list_guests[id_guest-1])
                    th.start()
                    # th.join()
                    print(f"{list_guests[id_guest-1].name} сел(-а) за стол номер {count_table}")
                    count_table += 1
                    break

            else:
                self.que.put(list_guests[id_guest-1])
                print(f"{list_guests[id_guest-1].name} в очереди")
                # print("состав очереди:", list(self.que.__dict__['queue']))
        # for thread in threading.enumerate():
        #     print("Имя потока %s." % thread.name)
        print()

    def end_service(self, table):

        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
        print(f'Стол номер {table.number} свободен\n')

        table.guest = None


    def discuss_guests(self):
        to_end = False
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", self.que.empty())
        # while not (self.que.empty()) or not Cafe.is_table_empty(table for table in self.tables):
        # while not to_end:
        while not (self.que.empty()) or not (to_end):

            for table in self.tables:

                if not (table.guest is None) and not (table.guest.is_alive()): #условие 1, условие 2
                    # print(f"Работает условие 1: за столом {table.number} есть гость {not (table.guest is None)}")
                    # print(f"Работает условие 2: поток гостя {table.guest.name} не жив: {not (table.guest.is_alive())}")
                    # print("Условия работают AND ОДНОВРЕМЕННО")
                    self.end_service(table)
                    table.guest = None

                if not (self.que.empty()) and table.guest is None:
                    table.guest = self.que.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}\n')
                    th = table.guest
                    th.start()
                    # print(f"Остаток в очереди: {list(self.que.__dict__['queue'])}")
                    # print(f"Гость {table.guest.name} за столом {table.number}")

                    if self.que.empty():
                        # print("Очередь пустая")
                        for table in self.tables:
                            # print(table.guest.name, "остался за столом №", table.number)
                            if table.guest is not None:
                                table.guest.join()
                                self.end_service(table)
                                to_end = True
                                # break

if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
    # for t in cafe.tables:
    #     print(t.guest)

