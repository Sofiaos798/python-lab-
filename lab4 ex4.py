def reverse_list():
    A = list(map(int, input('Введіть список чисел через пробіл: ').split()))
    print("Початковий список:", A)

    A.reverse()

    print("Список у зворотному порядку:", A)
    return A

reverse_list()
