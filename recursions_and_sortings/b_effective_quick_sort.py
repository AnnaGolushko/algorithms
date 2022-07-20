# ID 69442107

def partition(arr, left, right):
    i = left - 1
    pivot = arr[right]

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    # функция возвращает индекс, на который встал опорный элемент
    # после разделения части массива на меньше и больше чем опорный
    return i+1


def quicksort_inplace(arr, left, right):
    if left >= right:
        return None

    p_idx = partition(arr, left, right)
    quicksort_inplace(arr, left, p_idx-1)
    quicksort_inplace(arr, p_idx+1, right)


def normalize_array_to_sort(raw_data):
    # Кол-во решенных задач переводим в отриц. число для сравнения списков
    raw_data[1] = - int(raw_data[1])
    raw_data[2] = int(raw_data[2])
    # возвращаем данные в порядке лексикографического сравнения эл-ов в списках
    # 1-число решенных задач, 2-штраф, 0-логин
    return [raw_data[1], raw_data[2], raw_data[0]]


if __name__ == "__main__":
    number = int(input())
    array = [normalize_array_to_sort(input().split()) for _ in range(number)]

    quicksort_inplace(array, left=0, right=number-1)

    for row in array:
        print(row[2])
