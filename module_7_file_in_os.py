import os, time

if __name__ == "__main__":

    directory = os.getcwd()
    # directory = ".."
    list_files = os.walk(directory)

    for root, dirs, files in os.walk(directory):
        for file in files:

            filepath = os.path.join(root,file)

            filetime = os.path.getatime(filepath)

            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

            filesize = os.path.getsize(filepath)

            parent_dir = os.path.dirname(filepath)

            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

