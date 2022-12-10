from collections import defaultdict


class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.parent = parent
        self.locked = {}
        self.graph = defaultdict(list)
        for i, v in enumerate(parent):
            self.graph[v].append(i)

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if num not in self.locked or self.locked[num] != user:
            return False
        del self.locked[num]
        return True

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        def check_ancestor(num):
            """
            does not have any locked ancestors
            :return:
            """
            if num in self.locked:
                return False
            elif num == -1:
                return
            else:
                return check_ancestor(self.parent[num])

        flag = False
        def check_descendant(num):
            """
            at least one locked descendant
            :param num:
            :return:
            """
            nonlocal flag
            for child in self.graph[num]:
                if child in self.locked:
                    del self.locked[child]
                    flag = True
                check_descendant(child)
            return flag

        if num in self.locked:
            return False
        if not check_ancestor(num) or not check_descendant(num):
            return False
        self.locked[num] = user
        return True







# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)


if __name__ == "__main__":
    parent = [-1, 0, 0, 1, 1, 2, 2]
    obj = LockingTree(parent)
    print(obj.graph)
    param_1 = obj.lock(2, 2)
    print(obj.locked)
    # param_3 = obj.upgrade(num,user)