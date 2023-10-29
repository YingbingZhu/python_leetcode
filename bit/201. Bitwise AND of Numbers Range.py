class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0

        # find the common MSB(most significant bits).
        while left != right:
            left = left >> 1
            right = right >> 1

            shift += 1

        print(shift)
        return right << shift
