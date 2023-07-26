class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)
        while l < r:
            mid = (l + r) // 2
            left = arr[mid - 1]
            right = arr[mid + 1]
            if left < arr[mid]:
                if arr[mid] > right:
                    return mid
                else:
                    l = mid + 1
            else:
                r = mid
        return l
