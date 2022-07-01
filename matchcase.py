"""
в python 3.10 вышел новый оператор - match/case.
pattern matching - это не просто оператор для сравнения некоторой переменной со значениями,
это целый механизм для проверки данных, их распаковки и управления потоком выполнения.
"""

# def main(a1, b1, operation1):
#     match operation1:
#         case "+":
#             print(a+b)
#         case "-":
#             print(a-b)
#         case "*":
#             print(a*b)
#         case "/":
#             print(a/b)
#         case _:
#             raise ArithmeticError("Unknown operation")
#
#
# a = int(input("Введите первый операнд"))
# b = int(input("Введите второй операнд"))
# operation = input("Введите вид арифметической операции")
#
# main(a, b, operation)

###############################
# def load(links):
#     print("Загружаем", links)
#
#
# def main(data):
#     values = data.split("~")
#     match values:
#         case "load", *links:
#             load(links)
#         case _:
#             print("Unknown command")
#
#
# if __name__ == '__main__':
#     main("loading~http://example.com/files/test.txt~http://example.com/files/test1.txt")

################################
# def testcase(string):
#     string = string.split("~")
#     match string:
#         case name, "1" | "2" as access, request:
#             print("Пользователь {} получил доступ к функции {} с правами {}".format(name, request, access))
#         case _:
#             print("Unknown command")
#
#
# if __name__ == '__main__':
#     testcase("Djohn~3~load")
############################


def main(data_dictionary):
    match data_dictionary:
        case {"name": str(name), "access": 1 | 2 as access, "request": "load" as request}:
            print("Пользователь {} получил доступ к функции {} с правами {}".format(name, request, access))
        case _:
            print("Неудача")


if __name__ == '__main__':
    main({"name": "Daniil", "access": 2, "request": "load"})
