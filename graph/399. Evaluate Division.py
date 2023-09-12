class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        m = defaultdict(dict)
        for i, v in enumerate(equations):
            a = v[0]
            b = v[1]
            m[a][b] = values[i]
            m[b][a] = 1/values[i]
        
        def dfs(a, b, visited):
            if a not in m or b not in m:
                return -1
            if b in m[a]:
                return m[a][b]

            for i in m[a]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, b, visited)
                    if temp != -1:
                        return m[a][i] * temp
            return -1

        # for q in queries:
        res = []
        for q in queries:
            res.append(dfs(q[0], q[1], set()))
        return res
