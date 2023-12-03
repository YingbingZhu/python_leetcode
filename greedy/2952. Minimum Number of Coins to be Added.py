class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        cur_max = 0
        ans = 0
        for coin in coins:
            while coin > cur_max + 1 and cur_max < target:
                ans += 1
                cur_max += cur_max + 1
            # like prefix sum
            cur_max += coin
            if cur_max >= target:
                break
        
        while cur_max < target:
            cur_max += cur_max + 1
            ans += 1
        
        return ans

                