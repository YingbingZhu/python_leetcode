class Solution(object):
    def longestCycle(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        timestamps = [0] * len(edges)
        timestamp = 1
        
        res = -1

        for i in range(len(edges)):
            if timestamps[i] == 0:
                current_node = i
                start = timestamp
                while timestamps[current_node] == 0 and current_node != -1:
                    timestamps[current_node] = timestamp
                    timestamp += 1
                    current_node = edges[current_node]
                if current_node != -1 and timestamps[current_node] >= start:
                    res = max(res, timestamp - timestamps[current_node])
        return res