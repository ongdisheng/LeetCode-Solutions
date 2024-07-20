class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Time: O(m) where m = length of word
        Space: O(m)
        """
        # start from root node
        cur = self.root

        # iterate over every character in the word
        for char in word:

            # character not exists in trie yet
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            # update current
            cur = cur.children[char]
        
        # update end of word
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        """
        Time: O(26 ^ m) where m = length of word
        Space: O(26 ^ m) due to recursion stack
        """

        def dfs(node, index):
            # retrive current node
            cur = node

            # base case
            # reach end of word
            if index == len(word):
                return cur.end_of_word
            
            # retrieve current character
            char = word[index]

            # usual case
            if char != '.':
                if char not in cur.children:
                    return False
                return dfs(cur.children[char], index + 1)

            # special case `.`
            else:
                for child in cur.children:
                    if dfs(cur.children[child], index + 1):
                        return True
                return False

        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)