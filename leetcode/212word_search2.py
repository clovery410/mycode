from collections import defaultdict
class Solution(object):
    #solution1, TLE
    def findWords(self, board, words):
        def check(idx, r, c, word, mark):
            if idx >= len(word):
                return True
            if r < 0 or r >= m: return False
            if c < 0 or c >= n: return False

            if board[r][c] == word[idx] and not mark[r][c]:
                mark[r][c] = True
                if check(idx+1, r+1, c, word, mark) or check(idx+1, r-1, c, word, mark) or check(idx+1, r, c+1, word, mark) or check(idx+1, r, c-1, word, mark):
                    return True
                mark[r][c] = False
            return False

        m, n = len(board), len(board[0]) if len(board) > 0 else 0
        res = []
        start_point = defaultdict(list)
        for i in range(m):
            for j in range(n):
                start_point[board[i][j]].append((i, j))
                
        for word in set(words):
            if word[0] in start_point:
                for r, c in start_point[word[0]]:
                    mark = [[False] * n for x in range(m)]
                    if check(0, r, c, word, mark):
                        res.append(word)
                        break
        return res

#solution2, use trie + DFS
class TrieNode(object):
    def __init__(self):
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                new_child = TrieNode()
                current.children[c] = new_child
            current = current.children[c]
        current.children['_end_'] = '_end_'

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.children: return False
            current = current.children[c]
        return True if '_end_' in current.children else False

    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.children: return False
            current = current.children[c]
        return True

class Solution2(object):
    def findWords(self, board, words):
        def dfs(r, c, path, trie):
            if '_end_' in trie:
                res.append(path)
                #be carefull cannot write return here since although you find an end of a word here, but there might be longer word not ending yet, still need to recurse
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] not in trie:
                return
            cur_s = board[r][c]
            board[r][c] = '#'   #this is used as marking this word visited
            dfs(r+1, c, path+cur_s, trie[cur_s])
            dfs(r-1, c, path+cur_s, trie[cur_s])
            dfs(r, c+1, path+cur_s, trie[cur_s])
            dfs(r, c-1, path+cur_s, trie[cur_s])
            board[r][c] = cur_s   #change the visited mark back

        # build Trie
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['_end_'] = '_end_'   # denote here exists the end of a word

        # iterate the starting point within the board, then call dfs
        m, n = len(board), len(board[0]) if len(board) > 0 else 0
        res = []
        for i in range(m):
            for j in range(n):
                dfs(i, j, '', trie)
        return list(set(res))   # use set to deal with duplicate

if __name__ == "__main__":
    board = [['o','a','a','n'],
             ['e','t','a','e'],
             ['i','h','k','r'],
             ['i','f','l','v']]
    words = ["oath","pea","eat","rain","taea"]
    sol = Solution()
    print sol.findWords(board, words)
    sol2 = Solution2()
    print sol2.findWords(board, words)
