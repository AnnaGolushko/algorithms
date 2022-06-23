from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    result_list = []
    for i in range(0, len(a)):
        result_list.append(a[i])
        result_list.append(b[i])

    # Здесь реализация вашего решения
    return result_list

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))