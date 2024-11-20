from time import sleep
import threading
import time

def write_words(word_count, file_name):

    with open(file_name,'w',encoding='utf-8') as file_:
        for count_ in range(word_count+1):
            file_.write(f"Какое-то слово № {count_}")
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print(f"Работа потоков {end_time-start_time}sec")


thread_1 = threading.Thread(target=write_words(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words(100, 'example8.txt'))

start_time = time.time()
thread_1.start()
thread_1.join()
thread_2.start()
thread_2.join()
thread_3.start()
thread_3.join()
thread_4.start()
thread_4.join()
end_time = time.time()
print(f"Работа потоков {end_time-start_time}sec")