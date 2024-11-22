import os
from os import listdir
import multiprocessing
import time




def read_info(name):
    all_data = []
    with open(name,"r",encoding='utf-8') as file:
        while True:
            r_line = file.readline()
            if len(r_line) == 0:
                break
            else:
                all_data.append(r_line)
                # print(file.name,":", r_line)



if __name__ == '__main__' :
    os.chdir('mod10_files')
    list_files = listdir()
    print("Список используемых файлов:", list_files)


    #     ЛИНЕЙНЫЙ РЕЖИМ:

    start_time = time.time()
    for filename in list_files:
        read_info(filename)
    end_time = time.time()
    print("Время выполнения кода в ЛИНЕЙНОМ режиме:", end_time - start_time, "sec")

    #     МНОГОПРОЦЕССОРНЫЙ РЕЖИМ:

    start_time = time.time()
    with multiprocessing.Pool(processes=len(list_files)) as pool:
        pool.map(read_info,list_files)

    end_time = time.time()
    print("Время выполнения кода в МНОГОПРОЦЕССОРНОМ режиме:", end_time-start_time,"sec")

