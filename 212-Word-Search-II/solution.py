class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        """
        Time: O(m) where m = length of word
        Space: O(m)
        """
        # retrieve current node
        cur = self

        for char in word:

            # current character not in trie
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]
        
        # mark end of word
        cur.end = True
    
    def pruneWord(self, word):
        # retrieve current node
        cur = self

        # retrieve node and key pairs
        node_key = []
        for char in word:
            node_key.append((cur, char))
            cur = cur.children[char]

        # delete those nodes without children
        for parent_node, child_key in reversed(node_key):
            target_node = parent_node.children[child_key]
            if len(target_node.children) == 0:
                del parent_node.children[child_key]
            else:
                return


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Time: O(m * n * 4 ^ mn)
        Space: O(m * n) due to recursive stack
        """
        # create root node for trie
        root = TrieNode()

        # insert word into trie
        for w in words:
            root.addWord(w)

        # retrieve number of rows and columns
        rows, cols = len(board), len(board[0])
        res, visit = [], set()

        def dfs(r, c, node, word):
            # base case
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visit or 
                board[r][c] not in node.children):
                return
            
            # mark current coordinates as visited
            visit.add((r, c))

            # update node and word
            node = node.children[board[r][c]]
            word += board[r][c]

            # target word exists in board
            if node.end:
                res.append(word)
                node.end = False
                root.pruneWord(word)
            
            # recursive case
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            # remove current coordinates from visited
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, '')
        
        return res