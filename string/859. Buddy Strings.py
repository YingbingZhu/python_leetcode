class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        
        firstIdx = secondIdx = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if firstIdx == -1:
                    firstIdx = i
                elif secondIdx == -1:
                    secondIdx = i
                else:
                    return False
        if secondIdx == -1:
            return False
        return s[firstIdx] == goal[secondIdx] and s[secondIdx] == goal[firstIdx]