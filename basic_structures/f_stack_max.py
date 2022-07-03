class Stack:
     def __init__(self):
         self.items = []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[-1]

     def size(self):
         return len(self.items)


def get_max(stack):
    if stack.size() == 0:
        return None
    
    return max(stack.items)

if __name__ == "__main__":
    n = int(input())
    stack = Stack()
    for i in range(n):
        command = input().strip()
        if command == 'get_max':
            print(get_max(stack))
        elif command == 'pop':
            if stack.size() == 0:
                print('error')
            else:
                stack.pop()
        elif command.startswith('push '):
            command = command.replace('push ', '')
            stack.push(int(command))
