# ID первой попытки 69039170, ID после исправления замечаний 69133276
from typing import List, Tuple


def nearest_zero(street_length: int, street: List[int]) -> List[int]:
    """Алгоритм реализует рассчет расстояний
    от каждого дома на улице до ближайшего пустого участка.

    Args:
        street_length (int): длина улицы
        street (List[int]): номера домов и пустые участки на улице

    Returns:
        List[int]: расстояния до ближайших пустых участков
    """
    left_border = 0
    # В цикле находим первый ноль слева - левую границу списка
    for i in range(street_length):
        if street[i] == 0:
            left_border = i
            break
    # Для домов слева от левой границы расставим расстояния
    distance = left_border  # Для самого левого дома расстояние максимальное
    for i in range(left_border):
        street[i] = distance
        distance -= 1
    # Проходим все остальные случаи, когда есть дома справа от нуля
    distance = 1
    for i in range(left_border+1, street_length):
        if street[i] != 0:  # Для домов после нуля увеличиваем расстояние на 1
            street[i] = distance
            distance += 1
        else:
            # Если встретили снова ноль, идем обратно до середины
            # и ставим расстояния увеличивая на 1
            distance = 1
            step_back = 1
            middle_distance = int((i + left_border)/2)
            for j in range(i - 1, middle_distance, -1):
                street[j] = step_back
                step_back += 1

            left_border = i  # Обновляем значение левой границы (нового нуля)

    return street


def read_input() -> Tuple[int, List[int]]:
    """
    Функция считывания данных из консоли.
    Первая строка: длина улицы n (1 ≤ n ≤ 10^6).
    Вторая строка: n целых неотрицательных чисел — номера
    домов и обозначения пустых участков на карте (нули).
    """
    n = int(input())
    houses = [int(symbol) for symbol in input().strip().split()]
    return n, houses


if __name__ == '__main__':
    n, houses = read_input()
    print(*nearest_zero(n, houses))
