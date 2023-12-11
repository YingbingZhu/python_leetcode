import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        heap = []
        for ch, cnt in [['a', a], ['b', b], ['c', c]]:
            if cnt > 0:
                heappush(heap, (-cnt, ch))

        while heap:
            cnt, ch = heappop(heap)
            if len(ans) > 1 and ans[-1] == ans[-2] == ch:
                if heap:
                    cnt2, ch2 = heappop(heap)
                    heappush(heap, (cnt, ch))
                    ans += ch2
                    if cnt2 < -1:
                        heappush(heap, (cnt2+1, ch2))
            else:
                ans += ch
                if cnt < -1:
                    heappush(heap, (cnt+1, ch))
        return ans
                

            
            
            