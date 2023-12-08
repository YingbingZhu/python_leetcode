class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:

        def cal(s):
            cnt = 0
            # 26 alphabets
            for i in range(1, 27):
                if i * k > len(s):
                    break
                # possible length of substring
                r = i * k
                m = Counter(s[:r])
                # frequency of count values
                freq = Counter(m.values())
                if freq[k] == i: 
                    cnt += 1
                # sliding window
                for index in range(len(s) - r):
                    # remove leftmost ch
                    freq[m[s[index]]] -= 1
                    m[s[index]] -= 1
                    # add new count value freq
                    freq[m[s[index]]] += 1


                    freq[m[s[index+r]]] -= 1
                    m[s[index+r]] += 1  
                    freq[m[s[index+r]]] += 1

                    if freq[k] == i: 
                        cnt += 1  
            return cnt


        i = 0
        ans = 0
        for r in range(1, len(word)):
            # divide
            if abs(ord(word[r]) - ord(word[r-1])) > 2:           
                ans += cal(word[i:r])
                i = r
        ans += cal(word[i:])

        return ans  
        