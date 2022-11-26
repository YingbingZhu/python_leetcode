class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mapping = {}
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            num = nums2[i]
            while stack and stack[-1] < num:
                mapping[stack[-1]] = num
                stack.pop()
            stack.append(num)

        for num in stack:
            mapping[num] = -1

        res = []
        for num in nums1:
            res.append(mapping[num])

        return res

