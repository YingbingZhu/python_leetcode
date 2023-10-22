class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i[0] for i in sorted(enumerate(mat), key=lambda x:sum(x[1]))][:k]
        