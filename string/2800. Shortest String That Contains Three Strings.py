class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:

        def combine(a, b):
            if b in a:
                return a
            for i in range(min(len(b), len(a)) - 1, -1, -1):
                if a[len(a) - i:] == b[:i]:
                    return a + b[i:]
            return a + b

        abc = combine(combine(a, b), c)
        acb = combine(combine(a, c), b)
        bac = combine(combine(b, a), c)
        bca = combine(combine(b, c), a)
        cab = combine(combine(c, a), b)
        cba = combine(combine(c, b), a)
        lst = [abc, acb, bac, bca, cab, cba]
        lst.sort(key=lambda s: (len(s), s))
        return lst[0]
