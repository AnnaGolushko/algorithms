

def calculations(array):
    
    if len(array) == 1:
        return array[0], str(len(array[0]))
    
    max_word_index = 0
    for index in range(1, len(array)):
        if (len(array[index]) > len(array[index - 1])):
            if (len(array[index]) > len(array[max_word_index])):
                max_word_index = index
            
    return array[max_word_index], str(len(array[max_word_index]))


def read_input():
    n = int(input())
    words_array = [symbol for symbol in input().strip().split()]
    return words_array


if __name__ == '__main__':
    words_array = read_input()
    print('\n'.join(calculations(words_array)))
