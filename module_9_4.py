from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'



def get_advanced_writer(file_name):

    def write_everything(*data_set):

        with open(file_name, 'w') as file_:
            for data_ in data_set:
                if type(data_) != str:
                    file_.write(str(data_)+'\n')
                else:
                    file_.write(data_+'\n')

    return write_everything

class MysticBall:

    from random import choice

    def __init__(self, *words_):
        self.words = tuple(words_)

    def __call__(self):
        return choice(self.words)



if __name__ == "__main__":

    a = list(map(lambda x, y: x == y, first, second))
    print(a)

    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())