class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.prev = self.next = self
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
        

    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        n = Node(key, value)
        self._add(n)
        self.cache[key] = n
        if len(self.cache) > self.size:
            n = self.next
            self._remove(n)
            del self.cache[n.key]


    def _add(self, node):
        p = self.prev
        p.next = node
        self.prev = node
        node.prev = p
        node.next = self

    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)