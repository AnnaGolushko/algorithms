# ID 69441998

def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1

    # сравниваем индексы, проверяем не пуст ли отрезок массива для поиска
    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            return middle

        # Проверка, попала ли середина на упорядоченную по неубыванию часть
        if nums[left] <= nums[middle]:
            # если да, то проверяем, лежит ли искомое число в этой части
            if nums[left] <= target < nums[middle]:
                # если да, то правую границу сдвигаем на 1 левее середины
                right = middle - 1
            else:
                # иначе наоборот будем дальше искать в правой части от середины
                left = middle + 1
        else:
            # Если середина меньше левой границы (попали на разрыв частей)
            # то проверяем, лежит ли искомое число правее середины
            if nums[middle] < target <= nums[right]:
                # если да, то левую границу сдвигаем на 1 правее середины
                left = middle + 1
            else:
                # иначе наоборот будем дальше искать в левой части от середины
                right = middle - 1
    return -1


if __name__ == "__main__":
    n = int(input())
    target = int(input())
    arr = [int(symbol) for symbol in input().strip().split()]
    print(broken_search(arr, target))
