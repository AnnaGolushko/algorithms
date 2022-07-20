from random import randint


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    smaller, equal, larger = [], [], []
    pivot = arr[randint(0, len(arr)-1)]

    for x in arr:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    array = ([29, 99, 27, 41, 66,
              28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44])

    print(quick_sort(array))
