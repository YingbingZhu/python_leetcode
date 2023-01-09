#!/usr/bin/env python
"""
 Created by ZhuYB at 2023/1/6
"""
import heapq


class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        sorted_tasks = sorted([(enqueue, process, index) for index, (enqueue, process) in enumerate(tasks)])
        order = []
        print(sorted_tasks)
        min_heap = []
        index = 0
        curr_time = 0
        # stop when no task are left in array and heap
        while index < len(tasks) or min_heap:
            if not min_heap and curr_time < sorted_tasks[index][0]:
                curr_time = sorted_tasks[index][0]

            while index < len(tasks) and curr_time >= sorted_tasks[index][0]:
                _, process, task_index = sorted_tasks[index]
                heapq.heappush(min_heap, (process, task_index))

                index += 1

            process, index = heapq.heappop(min_heap)

            curr_time += process
            order.append(index)

        return order








if __name__ == '__main__':
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    Solution().getOrder(tasks)