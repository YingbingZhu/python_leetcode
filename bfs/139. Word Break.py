class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        words = set(wordDict)
        q = deque([0])
        seen = set()
        length = len(s)
        while q:
            start = q.popleft()
            if start == length:
                return True
            for end in range(start+1, length+1):
                if end not in seen and s[start:end] in words:
                    seen.add(end)
                    q.append(end)
        return False
                
        
