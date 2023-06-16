class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snaps = {i: {0: 0} for i in range(length)}

    def set(self, index: int, val: int) -> None:
        self.snaps[index][self.snap_id] = val


    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        
    def get(self, index: int, snap_id: int) -> int:
        # search backward for value change
        while snap_id > 0 and snap_id not in self.snaps[index]:
            snap_id -= 1
        return self.snaps[index][snap_id]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)