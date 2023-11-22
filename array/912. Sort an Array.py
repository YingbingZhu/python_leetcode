class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(nums):
            if len(nums) == 1: return 
            mid = len(nums) // 2
            l = nums[:mid] 
            r = nums[mid:]
            merge_sort(l)
            merge_sort(r)
            merge_sorted(l, r, nums)
        
        def merge_sorted(a, b, nums):
            i = j = p = 0
            while i < len(a) and j < len(b):
                if a[i] > b[j]:
                    nums[p] = b[j]
                    j += 1
                else:
                    nums[p] = a[i]
                    i += 1
                p += 1
            nums[p:] = a[i:] if i < len(a) else b[j:]
        

        merge_sort(nums)
        return nums