class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) // 4
        cnt = 1
        cur = arr[0]
        for i in range(1, len(arr)):
            if cnt > threshold:
                return cur
            if arr[i] == arr[i-1]:
                cnt += 1
            else:
                cur = arr[i]
                cnt = 1
        return cur
        