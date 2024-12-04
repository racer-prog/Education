from pprint import pprint
import inspect

result = {}

class My_class:

    def __init__(self):
        attr_1 = "Атрибут 1"
        attr_2 = "Атрибут 2"

    def my_get_attr(self):
        pass

def introsp_class(obj):
    pass

def introsp_func(obj):
    pass

def introsp_module(obj):
    pass

def introspection_info(obj):

    # print(f'Исследуемый объект: {obj.__class__.__name__}')

    result['type'] = obj.__class__.__name__
    # result['type'] = type(obj)
    # print(f'Тип данных: {type(obj)}')

    result['module'] = inspect.getmodule(obj)
    # print(f'Модуль, к которому принадлежит объект: {inspect.getmodule(obj)}')

    result['methods'] = [a for a in dir(obj) if callable(getattr(obj, a))]
    # print(f'Методы объекта: ', result['methods'])

    result['attributes'] = [a for a in dir(obj) if not callable(getattr(obj, a))]
    # print(f'Атрибуты объекта: ', result['attributes'])

    return result



# a = My_class()

# number_info = introspection_info(a)

number_info = introspection_info(42)

print(number_info)