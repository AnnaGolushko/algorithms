

def calculations(n, temperature_points):
    count = 0
    if n == 1:
        return 1
    if (temperature_points[0] > temperature_points[1]):
        count += 1
    if (temperature_points[n-1] > temperature_points[n-2]):
        count += 1
    
    for elem in range(1, n-1):
        if ((temperature_points[elem] > temperature_points[elem - 1]) and
            (temperature_points[elem] > temperature_points[elem + 1])):
            count += 1

    return count


def read_input():
    n = int(input())
    temperature_points = [int(symbol) for symbol in input().strip().split()]
    return n, temperature_points


if __name__ == '__main__':
    n, temperature_points = read_input()
    print(calculations(n, temperature_points))
