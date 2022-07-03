class Node:  
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    max_element = 0
    list_max_elem = []
    
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.max_element = item
            self.list_max_elem.append(item)
            return
        
        if item >= self.max_element:
            self.max_element = item
            self.list_max_elem.append(item)
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop(self):
        if self.tail.value == self.max_element:
            self.list_max_elem.pop()
            if len(self.list_max_elem) > 0:
                self.max_element = self.list_max_elem[-1]

        if self.tail.prev == None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None


def show(node):
    while node:
        print(node.value)
        node = node.next

if __name__ == "__main__":   
    n = int(input())
    stack = DoublyLinkedList()
    for i in range(n):
        command = input().strip()
        if command == 'get_max':
            if stack.head == None:
                print('None')
            else:
                print(stack.max_element)
        elif command == 'pop':
            if stack.head == None:
                print('error')
            else:
                stack.pop()
        elif command.startswith('push '):
            command = command.replace('push ', '')
            stack.push(int(command))
