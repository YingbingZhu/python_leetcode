class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        heap = []
        for key in counter.keys():
            heapq.heappush(heap, (-counter[key], key))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res