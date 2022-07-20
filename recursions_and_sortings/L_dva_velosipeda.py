# базовый вариант бинарного рекурсивного поиска из урока
def binarySearch(arr, x, left, right):
    if right <= left:  # промежуток пуст
        return -1
        # промежуток не пуст
    mid = (left + right) // 2
    if arr[mid] == x:  # центральный элемент — искомый
        return mid
    elif x < arr[mid]:  # искомый элемент меньше центрального
        # значит следует искать в левой половине
        return binarySearch(arr, x, left, mid)
    else:  # иначе следует искать в правой половине
        return binarySearch(arr, x, mid + 1, right)
# изначально мы запускаем двоичный поиск на всей длине массива
# index = binarySearch(arr, x, left = 0, right = len(arr))


def recursive_binary_search(arr, x, left, right):
    if left-1 == right:  # промежуток пуст
        if left == len(arr):  # прошли весь массив, дошли до правой границы
            return -1  # и все элементы оказались меньше чем x
        else:
            return left + 1  # иначе в одном из вызовов находили эл-т >= х
    mid = (left + right) // 2
    if arr[mid] >= x:  # искомый элемент меньше центрального
        # значит следует искать в левой половине
        return recursive_binary_search(arr, x, left, mid-1)
    else:  # иначе следует искать в правой половине
        return recursive_binary_search(arr, x, mid + 1, right)


if __name__ == "__main__":
    n = int(input())
    array = [int(symbol) for symbol in input().strip().split()]
    s = int(input())
    day1 = recursive_binary_search(array, s, left=0, right=len(array)-1)
    if day1 == -1:
        day2 = -1
    else:
        day2 = recursive_binary_search(array, s*2, left=0, right=len(array)-1)

    print(day1, day2)
