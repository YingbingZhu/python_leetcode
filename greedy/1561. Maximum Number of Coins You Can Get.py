class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        ans = 0
        l = 0
        r = len(piles) - 1
        while l < r - 1:
            y = l + 1
            ans += piles[y]
            l = y + 1
            r -= 1
        return ans