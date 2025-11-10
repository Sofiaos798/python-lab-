def delete_even_indexes():
    A = list(map(int, input('Введіть список чисел через пробіл: ').split()))
    print("Початковий список:", A)

    result = []

    for i in range(len(A)):
        if i % 2 != 0:  
            result.append(A[i])

    print("Список після видалення елементів з парними індексами:", result)
    return result

delete_even_indexes()
