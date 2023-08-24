class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        sc = dict(sorted(counter.items(), key=lambda x:x[1], reverse=True))
        n = len(s)

        for c in sc:
            if sc[c] > (n + 1) // 2:
                return ""

        res = [""] * n
        p = 0
        while p < n:
            i = 0
            while res[i] != "":
                i += 1
            
            for k in sc:
                while i < n and sc[k] > 0: 
                    res[i] = k
                    sc[k] -= 1
                    i += 2
                    p += 1

        return ''.join(res)