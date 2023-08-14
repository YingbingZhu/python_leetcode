class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:

            heapq.heappush(heap, i*(-1))
        print(heap)
        while k > 0:
            num = heappop(heap)
            k -= 1
        return -num