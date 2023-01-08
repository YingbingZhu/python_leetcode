class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = [['#', 0]]
        for d in s:
            if stack[-1][0] == d:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([d, 1])
        return ''.join(i * j for (i, j) in stack)











if __name__ == '__main__':
    s = "abcd"
    k = 2
    Solution().removeDuplicates(s, k)