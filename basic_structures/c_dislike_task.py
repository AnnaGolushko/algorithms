# Comment it before submitting
class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

def get_node_by_index(node, index):
        while index:
                node = node.next_item
                index -= 1
        return node

def solution(head, index):
    if index == 0:
            head = head.next_item
            return head
    
    node_to_delete = get_node_by_index(head, index)
    previous_node = get_node_by_index(head, index-1)
    previous_node.next_item = node_to_delete.next_item
    return head 

def show(node):
    while node:
        print(node.value)
        node = node.next_item

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    show(new_head)
    # result is node0 -> node2 -> node3

if __name__ == "__main__":
    test()
