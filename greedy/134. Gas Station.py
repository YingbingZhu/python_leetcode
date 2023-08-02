class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        curr_tank = trip_tank = start = 0
        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]
            trip_tank += gas[i] - cost[i]
            #  if curr_tanl< 0, not best start
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        # if total gas >=0, start is the answer
        return start if trip_tank >= 0 else -1