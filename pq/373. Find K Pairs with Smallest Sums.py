class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []

        visited = set()
        def push(i, j):
            if i < len(nums1) and j < len(nums2) and (i, j) not in visited:
                heapq.heappush(pq, [nums1[i] + nums2[j], i, j])
                visited.add((i, j))

        push(0, 0)
        res = []
        while pq and len(res) < k:
            _, i, j = heapq.heappop(pq)
            res.append([nums1[i], nums2[j]])
            push(i+1, j)
            push(i, j+1)
        return res