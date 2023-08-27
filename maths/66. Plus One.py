class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p = len(digits) - 1
        digits[p] += 1
        while digits[p] == 10:
            digits[p] = 0
            if p == 0:
                digits.insert(0, 1)
            else:
                digits[p-1] += 1
                p -= 1
        return digits