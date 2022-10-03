# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a certain timestamp.
#
# Implement the TimeMap class:
#
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously,
# with timestamp_prev <= timestamp. If there are multiple such values,
# it returns the value associated with the largest timestamp_prev.
# If there are no values, it returns "".
class TimeMap(object):

    def __init__(self):
        self.dict = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        d = self.dict.get(key)
        if not d:
            d[key] = []
        d.append([timestamp, value])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        lst = self.dict.get(key)
        if not list:
            return ""
        if lst[0][0] > timestamp:
            return ""
        l = 0
        r = len(lst)
        while l < r:
            mid = (l + r) // 2
            if lst[mid][0] > timestamp:
                r = mid
            elif lst[mid][0] <= timestamp:
                l = mid + 1
        return lst[r-1][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)