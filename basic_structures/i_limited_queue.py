class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        return x

    def queue_size(self):
        return self.size


if __name__ == '__main__':
    n = int(input())
    queue_max_size = int(input())
    queue = Queue(queue_max_size)

    for i in range(n):
        command = input().strip()
        if command == 'size':
            print(queue.queue_size())
        elif command == 'pop':
            print(queue.pop())
        elif command == 'peek':
            print(queue.peek())
        elif command.startswith('push '):
            command = command.replace('push ', '')
            queue.push(int(command))
