#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/11/7
"""
from collections import defaultdict


# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache.
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        # store nodes
        self.d = defaultdict()
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        self.delete(key)
        self.add(key, self.d[key].value)
        return self.d[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.delete(key)
            self.add(key, value)
            return
        if self.size == self.capacity:
            self.delete(self.head.next.key)
        self.add(key, value)

    def add(self, key, value):
        node = Node(key, value)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.d[key] = node
        self.size += 1

    def delete(self, key):
        """
        delete note
        :param key:
        :return:
        """
        node = self.d[key]
        del self.d[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
