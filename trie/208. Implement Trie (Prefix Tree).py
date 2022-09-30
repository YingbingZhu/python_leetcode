#!/usr/bin/env python
"""
 Created by ZhuYB at 2022/9/29
"""


# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store
# and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
# and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix,
# false otherwise.


class Trie(object):

    def __init__(self):
        self.dict = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.dict
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        # use "-" to mark the end of word
        curr["-"] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.dict
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return "-" in curr

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.dict
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
