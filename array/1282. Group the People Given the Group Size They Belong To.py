class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = collections.defaultdict(list)
        res = []
        max_size = max(groupSizes)
        for i, v in enumerate(groupSizes):
            d[v].append(i)
        for s, l in d.items():
            
            if len(l) > s:
                for i in range(0, len(l), s):
                    res.append(l[i:i+s])
            else:
                res.append(l)
        return res
                 