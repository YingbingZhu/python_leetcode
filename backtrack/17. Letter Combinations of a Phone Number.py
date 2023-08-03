class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
        }
        res = []
        if not digits: return res
        def dfs(i, cur):
            if i > len(digits)-1:
                res.append(cur)
                return
            for d in mapping[digits[i]]:
                dfs(i+1, cur+d)
        dfs(0, '')
        return res
        # (1) s + [x] returns a new list, without modifying s.
        # (2) s.append(x) modifies s.
        # If you want to re-use s afterwards, in case (1) you can reuse s directly, but in case (2) you need to pop x from s first.