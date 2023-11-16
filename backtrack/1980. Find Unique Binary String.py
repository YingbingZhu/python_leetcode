class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        combs = []
        def backtrack(i, cur):
            if i == len(nums):
                return cur if cur not in nums else None
            
            for nxt in ['1', '0']:
                res = backtrack(i+1, cur+nxt)
                if res:
                    return res


        return backtrack(0, '')