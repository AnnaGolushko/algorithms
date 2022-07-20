def merge(arr: list, left: int, mid: int, right: int) -> list:
    # из полученных интервалов получаем два отсортированных массива
    left_part = arr[left:mid]
    right_part = arr[mid:right]

    result = [0] * len(arr[left:right])
    # сливаем результаты
    i, r, k = 0, 0, 0
    while i < len(left_part) and r < len(right_part):
        # выбираем, из какого массива забрать минимальный элемент
        if left_part[i] <= right_part[r]:
            result[k] = left_part[i]
            i += 1
        else:
            result[k] = right_part[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while i < len(left_part):
        result[k] = left_part[i]  # перенеси оставшиеся элементы left в result
        i += 1
        k += 1

    while r < len(right_part):
        result[k] = right_part[r]  # перенеси оставшиеся эл-ты right в result
        r += 1
        k += 1

    arr[left:right] = result
    return arr


def merge_sort(arr: list, left: int, right: int) -> None:
    # базовый случай рекурсии
    if len(arr[left:right]) < 2:
        return arr[left:right]

    mid = left + (right - left)//2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)

    return merge(arr, left, mid, right)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == "__main__":
    test()
