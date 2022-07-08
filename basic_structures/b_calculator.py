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


def calculator(polski_expression):
    n = len(polski_expression)
    stack = DoublyLinkedList()
    result = 0
    for i in range(n):
        if polski_expression[i] in '+-*/':
            number_2 = stack.pop()
            number_1 = stack.pop()
            if polski_expression[i] == '+':
                result = number_1 + number_2
            elif polski_expression[i] == '-':
                result = number_1 - number_2
            elif polski_expression[i] == '*':
                result = number_1 * number_2
            elif polski_expression[i] == '/':
                result = number_1 // number_2

            stack.push(result)
        else:
            number = int(polski_expression[i])
            stack.push(number)

    return stack.pop()


if __name__ == "__main__":
    polski_expression = [symbol for symbol in input().strip().split()]
    print(calculator(polski_expression))
