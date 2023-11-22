class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m = p = g = 0
        n = len(garbage)
        ms = [i for i in range(n) if 'M' in garbage[i]]
        ps = [i for i in range(n) if 'P' in garbage[i]]
        gs = [i for i in range(n) if 'G' in garbage[i]]
        if ms:
            max_m = max(ms)
            for i in range(max_m+1):
                m += (0 if i == 0 else travel[i-1]) + garbage[i].count('M') 
        if ps:
            max_p = max(ps)
            for i in range(max_p+1):
                p += (0 if i == 0 else travel[i-1]) + garbage[i].count('P') 
        if gs:
            max_g = max(gs)
            for i in range(max_g+1):
                g += (0 if i == 0 else travel[i-1]) + garbage[i].count('G') 
        return g + p + m
            
        