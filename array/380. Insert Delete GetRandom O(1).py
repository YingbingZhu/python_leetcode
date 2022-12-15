#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/12
"""
from random import randint


class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.d = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.nums.append(val)
        self.d[val] = len(self.nums) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        # copy last element to deleted position
        index = self.d[val]
        last = self.nums[-1]
        self.nums[index] = last
        self.d[last] = index
        del self.d[val]
        self.nums.pop()
        return True


    def getRandom(self):
        """
        :rtype: int
        """
        return self.nums[randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

