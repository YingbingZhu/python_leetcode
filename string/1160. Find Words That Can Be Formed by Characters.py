class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for w in words:
            m = Counter(chars)
            p = 0
            while p < len(w):
                if w[p] in m and m[w[p]] > 0:
                    m[w[p]] -= 1
                    p += 1
                else:
                    break
            print(w, p)
            if p == len(w):
                ans += p
            print(ans)
        return ans