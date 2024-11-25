import requests
from lxml import etree
import datetime


# список валют с кодами
all_currency_link = 'http://www.cbr.ru/scripts/XML_val.asp?d=0'
# курсы валют на сегодняшний день
currency_value_link = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='+datetime.date.today().strftime('%d/%m/%Y')

# get-запрос по ссылке, получаем xml-данные
response = requests.get(all_currency_link)
# разбираем xml на элементы
root = etree.fromstring(response.content)


dict_currency = {}
name = ''
code = ''
# Находим элементы с нужными тэгами, формируем словарь
for i in root.getchildren():
    for e in i.getchildren():
        # print(e.tag, e.text)
        if e.tag == "Name":
            name = e.text
        if e.tag == "ParentCode":
            code = e.text
        dict_currency[name] = code

# get-запрос по ссылке с курсами валют
response_2 = requests.get(currency_value_link)
root_2 = etree.fromstring(response_2.content)


dict_currency_value = {}
name_2 = ''
value = ''
nominal = ''
# Находим элементы с нужными тэгами, формируем словарь
for i in root_2.getchildren():
    for e in i.getchildren():
        # print(e.tag, e.text)
        if e.tag == "Nominal":
            if e.text == '1':
                nominal = ''
            else:
                nominal = e.text
        if e.tag == "Name":
            name_2 = e.text
        if e.tag == "Value":
            value = e.text

        if name_2 and value:
            if nominal == "":
                dict_currency_value[name_2] = f"{value} рублей за единицу"
            else:
                dict_currency_value[name_2] = f"{value} рублей за {nominal} единиц"


print(dict_currency)
print(dict_currency_value)




