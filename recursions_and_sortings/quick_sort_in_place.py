from random import randint


def create_array(size=10, max=50):
    return [randint(0, max) for _ in range(size)]


def partition(arr, low, high):
    i = low - 1
    # выбираем крайний справа элемент в качестве опорного
    pivot = arr[high]

    # проходим по заданной части массива и сравниваем элементы
    # с опорным. Если эл <= опорному, то меняем местами с тем элементом,
    # который шел до этого меньшего.
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # если при проходе заданной части массива ни один элемент
    # не оказался меньше или равен опорному (pivot),
    # то меняем местами с опорным
    arr[i+1], arr[high] = arr[high], arr[i+1]
    # функция возвращает индекс, на который встал опорный элемент
    # после разделения части массива на меньше и больше чем опорный
    return i+1


def quicksort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    # если отрезок не пуст, то продолжаем вызовы функций
    # а иначе (если low >= high), то происходит return None
    # и это можно считать базовым случаем, просто он не прописан явно
    if low < high:
        p_idx = partition(arr, low, high)  # partition around pivot
        quicksort_inplace(arr, low, p_idx-1)  # sort lower half
        quicksort_inplace(arr, p_idx+1, high)  # sort upper half


if __name__ == "__main__":
    # arr = create_array()
    # arr = ([29, 99, 27, 41, 66,
    #         28, 44, 87, 19, 31, 76, 58, 12, 21])
    arr = [29, 99, 27, 12, 66, 19, 44, 10]
    print("Unsorted:", arr)
    quicksort_inplace(arr)
    print("Sorted:", arr)
