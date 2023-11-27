class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        hBars.sort()
        vBars.sort()

        mxh = mxv = 1
        i = 0
        while i < len(hBars):
            cnt = 1
            j = i + 1
            while j < len(hBars) and hBars[i] + cnt == hBars[j]:
                j += 1
                cnt += 1
            mxh = max(mxh, cnt)
            i = j

        print(mxh)
        
        i = 0
        while i < len(vBars):
            cnt = 1
            j = i + 1
            while j < len(vBars) and vBars[i] + cnt == vBars[j]:
                j += 1
                cnt += 1
            mxv = max(mxv, cnt)
            i = j
  

        return (min(mxh, mxv) + 1) ** 2
                 
