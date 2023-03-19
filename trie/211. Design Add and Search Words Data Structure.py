class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if current_node.children[idx] is None:
                current_node.children[idx] = TrieNode()
            current_node = current_node.children[idx]
        current_node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(index, current_node):
            if index == len(word):
                return current_node.is_end
            ch = word[index]
            if ch == '.':
                for i in range(26):
                    if current_node.children[i] is not None and dfs(index+1, current_node.children[i]):
                        return True
                return False
            else:
                idx = ord(ch) - ord('a')
                if current_node.children[idx] is None:
                    return False
                return dfs(index+1, current_node.children[idx])
        return dfs(0, self.root)



