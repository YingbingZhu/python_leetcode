class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        m = defaultdict(list)
        for e in edges:
            m[e[0]].append(e[1])
            m[e[1]].append(e[0])

        @cache
        def dfs(node, prev, is_healthy):
            if len(m[node]) == 1 and node != 0:
                return values[node] if is_healthy else 0

            # dont take current node
            leave = 0
            for child in m[node]:
                if child != prev:
                    leave += dfs(child, node, True)

            # take
            take = values[node]
            for child in m[node]:
                if child != prev:
                    take += dfs(child, node, is_healthy)

            return max(take, leave)

        return dfs(0, -1, False)




