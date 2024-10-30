import os, time

# list_all_files = []
# list_dir = []
# list_files = []
#
# def add_all_files(dir_:str):
#     list_files = os.listdir(dir_)
#     print(list_files)
#     for name_ in list_files:
#         list_all_files.append(os.path.abspath(name_))
#     # return list_files
#
# def sort_names(list_:[]):
#     while len(list_all_files) != 0:
#         for name_ in list_:
#             if os.path.isdir(name_) == True:
#                 # print(f"{name_} - Директория")
#                 list_dir.append(name_)
#                 list_all_files.remove(name_)
#
#             else:
#                 # print(f"{name_} - Файл")
#                 list_files.append(name_)
#                 list_all_files.remove(name_)




if __name__ == "__main__":
    # add_all_files('.')
    # sort_names(list_all_files)
    # print('Директории: ', list_dir)
    # print('Файлы: ',list_files)
    # print(list_all_files)

    directory = '.'
    list_files = os.walk(directory)
    # print(list_files.)

    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.abspath(file)

            filetime = os.path.getatime(file)

            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

            filesize = os.path.getsize(file)

            parent_dir = os.path.dirname(filepath)

            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

