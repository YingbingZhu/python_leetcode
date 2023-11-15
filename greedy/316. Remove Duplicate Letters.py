class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_p = {}
        for i, v in enumerate(s):
            last_p[v] = i
        
        stack = []
        visited = set()
        for i, v in enumerate(s):
            # new chr not added yet
            if v not in visited:
                # new chr is smaller then current end, and current end is not its last pos
                while stack and stack[-1] > v and last_p[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(v)
                visited.add(v)
        return ''.join(stack)
        

            