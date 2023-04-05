class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Time: O(m) where m = length of word
        Space: O(m)
        """
        # start from root node
        cur = self.root

        # iterate over every character in the word
        for c in word:

            # character not exists in trie yet
            if c not in cur.children:
                cur.children[c] = TrieNode()
            
            # update current 
            cur = cur.children[c]
        
        # update end of word
        cur.end_of_word = True
        

    def search(self, word: str) -> bool:
        """
        Time: O(m) where m = length of word
        Space: O(1)
        """
        # start from root node
        cur = self.root

        # iterate over every character in the word
        for c in word:

            # character not exists in trie 
            if c not in cur.children:
                return False
            
            # update current 
            cur = cur.children[c]
        
        # verify if end of word has been reached
        return cur.end_of_word


    def startsWith(self, prefix: str) -> bool:
        """
        Time: O(m) where m = length of prefix
        Space: O(1)
        """
        # start from root node
        cur = self.root

        # iterate over every character in the prefix
        for c in prefix:

            # character not exists in trie 
            if c not in cur.children:
                return False
            
            # update current 
            cur = cur.children[c]
        
        # all characters in prefix exist in trie
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)