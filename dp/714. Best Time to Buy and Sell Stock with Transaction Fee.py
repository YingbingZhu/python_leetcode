class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # cash in hand without buy at first day
        cash_w_share = -prices[0]
        # cash in hand with buying at first day
        cash_no_share = 0
        for i in range(1, len(prices)):
            cash_w_share = max(cash_w_share, cash_no_share-prices[i])
            cash_no_share = max(cash_no_share, cash_w_share+prices[i]-fee)
        return cash_no_share