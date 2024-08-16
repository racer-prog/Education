import random


num_list = []


def list_create(start=3,end=20):
    for i in range(start, end + 1):
        num_list.append(i)
    return num_list

def left_num():
    left = list_create()[random.randint(list_create()[0],len(list_create()))]
    return left

def spisok_par(n=20):

    spisok = []
    for i in range(n,0,-1):
        para = []
        if i >= 0 and n-i > 0:
            #print(n-i,'+',i)
            if (n-i) or i not in para:
                para.append(n-i)
                para.append(i)
            if [para[1],para[0]] not in spisok:
                spisok.append(para)

        else:
            continue
    return spisok



def algoritm(get_num):
    right_list = []
    #print('Пары числа ', get_num,': ')
    #print(''.join(str(spisok_par(get_num))))

    for i in range(get_num-1,0,-1):
        if get_num % i == 0:
            if len(spisok_par(i)) > 0:
                #print(i, 'делитель числа ', get_num, 'результат деления: ', get_num // i)
                #print('Список пар числа ', i, ':')
                for p in spisok_par(i):
                    #print(p)
                    right_list.append(p)
    for i in spisok_par(get_num):
        right_list.append(i)
    for i in right_list:
        if i[0] == i[1]:
            right_list.remove(i)
    #print('----------------')
    right_list = sorted(right_list)
    #print(right_list)
    #print('----------------')
    result = ''
    for x in right_list:
        for y in x:
            result += str(y)
    print("Число слева:", get_num, "Пароль:", result)




def result():
    for i in list_create(3,20):
        algoritm(i)


result()
