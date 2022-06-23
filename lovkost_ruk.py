# ID 69058415
from typing import Tuple


def play_the_game(max_fingers: int, matrix: str) -> int:
    """Функция реализует игру «Тренажёр для скоростной печати» (Ловкость рук).

    Args:
        max_fingers (int): max кол-во нажатий клавиш двумя игроками
        matrix (str): поле для игры из клавиш 4x4 (16 эл.)

    Returns:
        int: max кол-во баллов, которые два игрока могут набрать в игре
    """
    win_count = 0
    for time_point in range(1, 10):
        numbers_count = matrix.count(str(time_point))
        if max_fingers >= numbers_count and numbers_count != 0:
            win_count += 1
    return win_count


def read_input() -> Tuple[int, str]:
    """
    Функция считывания данных из консоли.
    1-ая строка: k (1 ≤ k ≤ 5)-кол-во одновременно нажатых клавиш одного игрока
    Еще четыре строки: по 4 символа в каждой строке.
    Каждый символ —– либо точка, либо цифра от 1 до 9.
    Символы одной строки идут подряд и не разделены пробелами.
    """
    max_fingers = int(input())*2
    game_matrix = ''
    game_matrix = ''.join([game_matrix + input() for line in range(4)])
    return max_fingers, game_matrix


if __name__ == "__main__":
    max_fingers, game_matrix = read_input()
    print(play_the_game(max_fingers, game_matrix))
