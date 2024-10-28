class Product():

    def __init__(self,name_:str, weight_:float, category_:str):
        self.name = name_
        self.weight = weight_
        self.category = category_

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():

    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name,'r') as file_:
            str_ = file_.read()
            #print(str_)
            return str_

    def add(self, *product:Product):
        with open(self.__file_name, 'a') as file_:
            __a = self.get_products()
            #print(__a)
            pr_spisok = [pr for pr in product]
            for i in pr_spisok:
                #print(i)
                if str(i) in __a:
                    print(f'Продукт {str(i)} уже есть в магазине')
                else:
                    file_.write(str(i)+'\n')



if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())



