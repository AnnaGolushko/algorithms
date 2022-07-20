def combinations(numbers, array, word):
    if numbers == '':
        array.append(word)
        return
    else:
        for letter in PHONE_LETTERS.get(numbers[0]):
            word += letter
            combinations(numbers[1:], array, word)
            word = word[:-1]


if __name__ == "__main__":
    numbers = input()
    array = []
    PHONE_LETTERS = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    combinations(numbers, array, word='')
    for combination in array:
        print(combination, end=' ')
