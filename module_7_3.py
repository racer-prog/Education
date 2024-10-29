from itertools import count


class WordsFinder():

    def __init__(self, *files_:str):
        self.file_names = []
        for file_ in files_:
            self.file_names.append(file_)

    def get_all_words(self):
        all_words = {}
        remove_char = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name,'r', encoding='utf-8') as str_file:
                str_ = str_file.read()
                for char in remove_char:
                    str_ = str_.replace(char,'')
                all_words[file_name] = str_.lower().split()

        return all_words

    def find(self, word):
        pos_world = {}
        word = word.lower()
        __all_words = self.get_all_words()
        for key_ in __all_words:
            #print(self.get_all_words()[key_])
            if word in __all_words[key_]:
                #print(key_)
                pos_world[key_] = __all_words[key_].index(word)+1
        #print(pos_world)
        return pos_world

    def count(self,word):
        count_world = {}
        word = word.lower()
        __count = 0
        __all_words = self.get_all_words()
        for key_ in __all_words:
            # print(self.get_all_words()[key_])
            if word in __all_words[key_]:
                for i in __all_words[key_]:
                    if i == word:
                        __count += 1
                # print(__count)
                # print(key_)
                # print(word)
                # count_world[key_] = count_world[key_] + 1
            count_world[key_] = __count
        # print(pos_world)
        return count_world


if __name__ == "__main__":

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    # finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
    # print(finder1.get_all_words())
    # print(finder1.find('Child'))
    # print(finder1.count('Child'))