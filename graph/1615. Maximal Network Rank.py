class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for a, b in roads:
            degrees[a] += 1
            degrees[b] += 1
        
        road_set = set(tuple(road) for road in roads)


        # find top two degrees
        sorted_degrees = sorted(set(degrees), reverse=True)
        max_deg = sorted_degrees[0]
        second_max_deg = sorted_degrees[1] if len(sorted_degrees) > 1 else 0
        index = [i for i, v in enumerate(degrees) if v == max_deg]
        second_index = [i for i, v in enumerate(degrees) if v == second_max_deg]

        # if there are two max
        if len(index) > 1:
            for i in index:
                x = [j for j in index if (i, j) not in road_set and (j, i) not in road_set and  i != j]
                # if connected
                if len(x):
                    return 2 * max_deg
            else:
                return 2 * max_deg - 1
        
        # only one max
        else:
            for j in second_index:
                if (index[0], j) not in road_set and (j, index[0]) not in road_set:
                    return max_deg + second_max_deg
            return max_deg + second_max_deg - 1
