class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        table = [0 for _ in range(days[-1]+1)]

        for i in range(days[-1]+1):
            if i not in days:
                table[i] = table[i-1]
            else:
                # use max to ensure day exist
                table[i] = min(
                    table[max(0, i-1)]+costs[0],
                    table[max(0, i-7)]+costs[1],
                    table[max(0, i-30)]+costs[2]
                )

        return table[-1]