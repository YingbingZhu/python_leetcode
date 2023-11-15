class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        wins = 0
        for i in range(1, len(arr), 1):
            if arr[i] > winner:
                winner = arr[i]
                wins = 1
            else:
                wins += 1
            if wins == k:
                return winner
        return winner


