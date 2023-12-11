class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        ls = moves.count('L')
        rs = moves.count('R')
        empty = len(moves) - ls - rs
        if ls > rs:
            return ls + empty - rs
        else:
            return rs + empty - ls
        
        