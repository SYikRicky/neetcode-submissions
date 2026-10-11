class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap: int = capacity
        self.cache: dict[int, int] = {}
        self.l_dummy, self.r_dummy = Node(0, 0), Node(0, 0)
        self.l_dummy.next, self.r_dummy.prev = self.r_dummy, self.l_dummy
    
    def remove_node(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert_node(self, node: Node) -> None:
        prev, nxt = self.l_dummy, self.l_dummy.next
        prev.next = node
        nxt.prev = node
    
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # change order
        # remove_node -> insert_node
        self.remove_node(self.cache[key])
        self.insert_node(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.r_dummy.prev
            self.remove_node(lru)
            del self.cache[lru.key]