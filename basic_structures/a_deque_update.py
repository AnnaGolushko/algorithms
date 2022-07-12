# ID 69330838, ID after review 1 69377676

class NoItemsInDequeException(Exception):
    def __init__(self):
        pass


class MaxItemsInDequeException(Exception):
    def __init__(self):
        pass


class Deque:
    """Класс Deque реализует структуру данных дек (двусторонняя очередь)
    по принципу кольцевого буффера с использованием массива ([] - list)"""
    def __init__(self, max_size):
        self.__deque = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    @property
    def is_full(self):
        return self.__size == self.__max_size

    @property
    def is_empty(self):
        return self.__size == 0

    def __count_index(self, elem, increase_param):
        return (
            (elem + 1) % self.__max_size
            if increase_param
            else (elem - 1) % self.__max_size
        )

    def push_front(self, value):
        """Метод push_front добавляет элемент в начало дека"""
        if self.is_full:
            raise MaxItemsInDequeException

        self.__deque[self.__head - 1] = value
        self.__head = self.__count_index(self.__head, False)
        self.__size += 1

    def push_back(self, value):
        """Метод push_back добавляет элемент в конец дека"""
        if self.is_full:
            raise MaxItemsInDequeException

        self.__deque[self.__tail] = value
        self.__tail = self.__count_index(self.__tail, True)
        self.__size += 1

    def pop_front(self):
        """Метод pop_front удаляет элемент из начала дека и возвращает его"""
        if self.is_empty:
            raise NoItemsInDequeException

        x = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = self.__count_index(self.__head, True)
        self.__size -= 1
        return x

    def pop_back(self):
        """Метод pop_back удаляет элемент из конца дека и возвращает его"""
        if self.is_empty:
            raise NoItemsInDequeException

        x = self.__deque[self.__tail - 1]
        self.__deque[self.__tail - 1] = None
        self.__tail = self.__count_index(self.__tail, False)
        self.__size -= 1
        return x


if __name__ == '__main__':
    count_commands = int(input())
    deque_size = int(input())

    deque = Deque(deque_size)

    for _ in range(count_commands):
        try:
            command = input().split(' ')
            if len(command) == 2:
                getattr(deque, command[0])(command[1])
            else:
                print(getattr(deque, command[0])())
        except NoItemsInDequeException:
            print('error')
        except MaxItemsInDequeException:
            print('error')
