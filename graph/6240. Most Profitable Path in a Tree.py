from collections import defaultdict, deque


class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        # visited array
        res = visited = [0] * len(amount)
        visited[0] = visited[bob] = 1

        graph = defaultdict(list)
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]

        alice = amount[0]
        queue = deque([(0, 0)])
        ans = float('-inf')
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for i in graph[node]:
                    if visited[i] == 0:
                        curr = node[1] + amount[i]
                        queue.append((i, curr))






        print(alice)
        return alice


if __name__ =="__main__":
    s = Solution()
    s.mostProfitablePath(edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6])