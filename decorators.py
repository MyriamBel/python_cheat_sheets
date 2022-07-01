"""
Декораторы - некоторая функция - обертка, которая перехватывает другую функцию и может внести изменения
в исполняемый ею код.
Можно выполнить некоторый код до или после базовой функции, таким образом можно изменять ее переменные
до вычислений или после, записать все данные в файл и многое другое.
Работа декораторов построена за счёт замыканий.
Замыкание - это функция внутри другой функции, она ссылается на переменные, объявленные во внешней функции.
Другое определение:
это такая функция, которая ссылается на локальные переменные (использует их в своём теле) в области видимости,
в которой она была создана.
Замыкающая функция может использоваться, когда необходимо создать некоторую функцию с заданной переменной,
 которая должна существовать и после завершения работы. По сути, замыкающая функция запоминает используемые ею
 переменные и они продолжают жить и после завершения работы внешней функции.
"""

##############################
# Замыкающая функция запоминает самое последнее состояние(до завершения внешней функции) аргумента в своей
# области видимости:


def outer():
    y = 1

    def inner(x):
        return x+y
    y = 10
    return inner


print(outer()(10))
# Так что в циклах нужно быть осторожными с замыканием - оно все разы выполнения сохранит только
# последний элемент цикла:
printers = []
for i in range(10):
    def printer():
        print(i)
    printers.append(printer)


# Как же запоминать то, что нужно и когда нужно?
# Как же нам починить пример с циклом, чтобы каждая функция печатала своё значение и не реагировала
# на дальнейшие изменения переменной цикла?
# Отвечаю: нужно замкнуть переменную в области видимости, которая завершится сразу же после создания замыкания!
# Этого можно добиться, завернув создание функции в… другую функцию! Вот код:

printers = []
for i in range(10):
    def make_printer(arg):
        def printer():
            print(arg)
        return printer
    p = make_printer(i)
    printers.append(p)
#########################

# Если нам необходимо несколько раз выполнить умножение на 5, то создадим одну функцию, которая будет умножать на
# 5 все переданные ей объекты:


def multiple(a):
    def helper(b):
        return a * b

    return helper


print(multiple(5)(2))
# То же самое, что:
multiple5 = multiple(5)
print(multiple5(2))

list_numbers = []
for i in range(0, 11):
    list_numbers.append(multiple5(i))
print(list_numbers)

print(multiple5('aaa '))

# def name(function):
#     def wrapper():
#         return "Hello, {}!".format(function())
#     return wrapper
#
#
# @name
# def hello():
#     return input("Enter your name")
#
#
# print(hello())
#
#########################
# def greet(function):
#     def wrapper_en():
#         return "Hello, {}!".format(function)
#     return wrapper_en()
#
#
# def greet_ru(function):
#     def wrapper_ru():
#         return "Привет, {}!".format(function())
#     return wrapper_ru()
#
#
# @greet
# @greet_ru
# def base_function():
#     return input("Enter your name: ")
#
#
# print(base_function)
#######################

# def decorator1(function):
#     def wrapper():
#         print("First message")
#         function()
#         print("Second message")
#     return wrapper()
#
#
# def decorator2():
#     print("Third message")
#
# decorator2 = decorator1(decorator2)
# decorator2()

############################
# def decorator(function):
#     def wrapper(*args, **kwargs):
#         function(*args, **kwargs)
#         print("decorator is done")
#     return wrapper
#
#
# @decorator
# def decorator2(name):
#     print("{}".format(name))
#
#
# decorator2("Python")
#################################

# def decorator(function):
#     def wrapper(*args):
#         print("Second decorator: {}".format(function(*args)*2))
#         return function(*args)*2
#     return wrapper
#
#
# def decorator3(function):
#     def wrapper(*args):
#         print("Third decorator: {}".format(function(*args)*10))
#         return function(*args)*10
#     return wrapper
#
#
# @decorator3
# @decorator
# def decorator2(a, b):
#     return a + b
#
#
# print(decorator2(1, 2))
