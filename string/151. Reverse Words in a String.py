class Solution:
    def reverseWords(self, s: str) -> str:
        lst = [i for i in s.split(' ') if i != '']
        return ' '.join(reversed(lst))