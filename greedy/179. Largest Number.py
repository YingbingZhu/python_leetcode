class LargestNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = ""
        largest_num = ''.join(sorted(map(str, nums), key=LargestNumKey))
        return '0' if largest_num[0] == '0' else largest_num


