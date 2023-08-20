class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = Counter(magazine)
        for s in ransomNote:
            if s not in m or m[s] == 0:
                return False
            m[s] -= 1
        return True