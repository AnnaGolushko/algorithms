def calculations(numbers):
    return numbers[0]*numbers[1]**2 + numbers[2]*numbers[1] + numbers[3]


def read_input():
    numbers = [int(symbol) for symbol in input().strip().split()]
    return numbers


if __name__ == '__main__':
    numbers = read_input()
    print(calculations(numbers))
