#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/12/15
"""
import heapq


# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
#
# Implement the SmallestInfiniteSet class:
#
# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

class SmallestInfiniteSet(object):

    def __init__(self):
        self.popped = set()
        self.minHeap = [1]

    def popSmallest(self):
        """
        :rtype: int
        """
        num = heapq.heappop(self.minHeap)
        self.popped.add(num)
        next_smallest = num + 1
        if not self.minHeap or (self.minHeap[0] != next_smallest):
            heapq.heappush(self.minHeap, next_smallest)

        return num

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)