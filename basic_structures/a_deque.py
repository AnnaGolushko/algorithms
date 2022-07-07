# ID 69330838
class Deque:
    """Класс Deque реализует структуру данных дек (двусторонняя очередь)
    по принципу кольцевого буффера с использованием массива ([] - list)"""
    def __init__(self, max_size):
        self.deque = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_front(self, value):
        """Метод push_front добавляет элемент в начало дека"""
        if self.size != self.max_size:
            self.deque[self.head - 1] = value
            self.head = (self.head - 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def push_back(self, value):
        """Метод push_back добавляет элемент в конец дека"""
        if self.size != self.max_size:
            self.deque[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print('error')

    def pop_front(self):
        """Метод pop_front удаляет элемент из начала дека и возвращает его"""
        if self.is_empty():
            return 'error'
        x = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return x

    def pop_back(self):
        """Метод pop_back удаляет элемент из конца дека и возвращает его"""
        if self.is_empty():
            return 'error'
        x = self.deque[self.tail - 1]
        self.deque[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return x


if __name__ == '__main__':
    count_commands = int(input())
    deque_size = int(input())

    deque = Deque(deque_size)

    for i in range(count_commands):
        command = input().strip()
        if command.startswith('push_front '):
            command = command.replace('push_front ', '')
            deque.push_front(int(command))
        elif command.startswith('push_back '):
            command = command.replace('push_back ', '')
            deque.push_back(int(command))
        elif command == 'pop_front':
            print(deque.pop_front())
        elif command == 'pop_back':
            print(deque.pop_back())
