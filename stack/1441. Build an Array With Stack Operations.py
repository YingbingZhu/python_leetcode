class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        currentIndex = 0
        ans = []
        for i in range(1, n+1):
            if currentIndex == len(target):
                return ans
            if target[currentIndex] == i:
                ans.append("Push")
                currentIndex += 1
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans
