class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # count 1 in data
        ones = sum(data)

        if ones <= 1:
            return 0


        window = cur = sum(data[:ones])
        l = 0
        r = ones
        while r < len(data):
            if data[l] == 1:
                cur -= data[l]
            if data[r] == 1:
                cur += 1
            l += 1
            r += 1
            window = max(window, cur)
        return ones - window

            