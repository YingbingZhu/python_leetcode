class MyHashSet(object):

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def _hash(self, key):
        """
        calculate the hash value for searching bucket
        """
        return key % self.size

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = self._hash(key)
        return key in self.buckets[index]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)