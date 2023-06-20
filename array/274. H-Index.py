class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        if citations[-1] >= len(citations):
            return len(citations)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return -1