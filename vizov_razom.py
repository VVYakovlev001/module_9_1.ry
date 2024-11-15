def apply_all_func(int_list, *functions):
    results = {}
    for fun in functions:
        #name = fun.__name__
        #result = fun(int_list)
        results.update({fun.__name__: fun(int_list)})
    return results

int_list = []

def min(int_list):  # - принимает список, возвращает минимальное значение из него.
    i = 0
    for i in range(len(int_list) - 1):
        if int_list[i] < int_list[i + 1]:
            result = int_list[i]
    return result


def max(int_list):  # - принимает список, возвращает максимальное значение из него.
    i = 0
    for i in range(len(int_list) - 1):
        if int_list[i] > int_list[i + 1]:
            result = int_list[i]
    return result


def len_(int_list):  # - принимает список, возвращает кол-во элементов в нём.
    result = len(int_list)
    return result


def sum(int_list):  # - принимает список, возвращает сумму его элементов.
    result = 0
    for i in int_list:
        result += i
    return result


def sorted_(int_list):  # - принимает список, возвращает новый отсортированный
    # список на основе переданного.
    result = sorted(int_list)
    return result


def midle(int_list):  # - принимает список, возвращает среднее значение его элементов.
    result = 0
    for i in int_list:
        result += i
    result = result / len_(int_list)
    return result


# min - принимает список, возвращает минимальное значение из него.
# max - принимает список, возвращает максимальное значение из него.
# len - принимает список, возвращает кол-во элементов в нём.
# sum - принимает список, возвращает сумму его элементов.
# sorted - принимает список, возвращает новый отсортированный список
# на основе переданного.



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
