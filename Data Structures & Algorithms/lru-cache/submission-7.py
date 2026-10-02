#implement as doubly-linked list: stores order of LRU, tail of linked list is most recently used
#head is least-recently-used
#hashmap to get values quickly

class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.cache = {}
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add(self, node: Node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        curr = self.head
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]
            newNode = Node(key, value)
            self.cache[key] = newNode
            self.add(newNode)

