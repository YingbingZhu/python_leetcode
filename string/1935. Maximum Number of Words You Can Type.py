class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        words = text.split(' ')
        count = len(words)
        for w in words:
            if set(brokenLetters) & set(w):
                count -= 1
        return count