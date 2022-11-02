class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        p = 0
        sign = 1
        num = 0
        while p < len(s) and s[p] == '':
            p += 1
        if p == len(s):
            return num
        if s[p] == '-':
            sign = -1
            p += 1
        elif s[p] == '+':
            sign = 1
            p += 1
        while p < len(s) and s[p].isdigit():
            curr = ord(s[p]) - ord('0')
            if num > (2 ** 31 - 1) // 10 or (num == (2 ** 31 - 1) // 10 and curr > 7):
                return 2 ** 31 - 1 if sign == 1 else -2 ** 31
            num = num * 10 + curr
            p += 1

        return sign * num
