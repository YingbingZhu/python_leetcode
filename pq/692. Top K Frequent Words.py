# Given an array of strings words and an integer k, return the k most frequent strings.
#
# Return the answer sorted by the frequency from highest to lowest.
# Sort the words with the same frequency by their lexicographical order.

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    # less than
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)
        heapq = []
        for word, freq in counter.items():
            node = Node(word, freq)
            if len(heapq) == k:
                heappushpop(heapq, node)
            else:
                heappush(heapq, node)
        res = []
        while heapq:
            res.append(heappop(heapq).word)
        return res[::-1]