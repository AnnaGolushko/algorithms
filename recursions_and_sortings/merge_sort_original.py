def merge_sort(array):
    if len(array) == 1:  # базовый случай рекурсии
        return array

    mid = len(array)//2
    lefthalf = array[:mid]
    righthalf = array[mid:]

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(lefthalf)

    # запускаем сортировку рекурсивно на правой половине
    right = merge_sort(righthalf)

    # заводим массив для результата сортировки
    result = [0] * len(array)

    # сливаем результаты
    i, r, k = 0, 0, 0
    while i < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[i] <= right[r]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while i < len(left):
        result[k] = left[i]  # перенеси оставшиеся элементы left в result
        i += 1
        k += 1

    while r < len(right):
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result


if __name__ == "__main__":
    array = [int(symbol) for symbol in input().strip().split()]
    print(*merge_sort(array))
