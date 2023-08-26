class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        s_pairs = sorted(pairs, key = lambda x:x[1])
        res = 0
        cur = float('-inf')
        
        for head, tail in s_pairs:
            if head > cur:
                cur = tail
                res += 1
            
        return res