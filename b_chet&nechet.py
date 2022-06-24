def calculations(x_in_list_format, k):
    x_string = ''
    for elem in x_in_list_format:
        x_string += elem
    
    return str(int(x_string) + k)


def read_input():
    n = int(input())
    x_in_list_format = [symbol for symbol in input().strip().split()]
    k = int(input())
    return n, x_in_list_format, k


if __name__ == '__main__':
    n, x_in_list_format, k = read_input()
    print(*calculations(x_in_list_format, k))
