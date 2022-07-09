# ID 69345577
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop(self):
        elem = self.tail
        if self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return elem.value


def calculator():
    OPERATIONS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x
    }

    stack = DoublyLinkedList()

    for polski_expression_item in input().strip().split():
        if polski_expression_item in '+-*/':
            operation = OPERATIONS.get(polski_expression_item)
            stack.push(operation(stack.pop(), stack.pop()))
        else:
            stack.push(int(polski_expression_item))

    return stack.pop()


if __name__ == "__main__":
    print(calculator())
