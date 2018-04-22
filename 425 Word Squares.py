from collections import defaultdict

class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """

    def initPrefix(self, words, dic):
        for item in words:
            dic[""].append(item)
            
            pre = ""
            for c in item:
                pre = pre + c
                dic[pre].append(item)
            
            
    def checkPrefix(self, l, nextWord, wordLen, dic, squares):
        for j in range(l+1, wordLen):
            pre = ""
            for k in range(l):
                pre = pre + squares[k][j]
            pre  = pre + nextWord[j]
            if pre not in dic:
                return False
        return True
    
    # l: current level, wordLen: num of levels 
    def dfs(self, l, wordLen, dic, squares, ans):
        if l == wordLen:
            ans.append(squares)
            return
        # i -- word, l -- character in a certain word, w-- all possible words to be in next position
        pre = ""
        for i in range(l):
            pre = pre + squares[i][l]                   
        w = dic[pre]                                                     # redundancy 1
         
        for item in w:
            if not self.checkPrefix(l, item, wordLen, dic, squares):     # redundancy 2
                continue
            self.dfs(l+1, wordLen, dic, squares.append(item), ans)



    def wordSquares(self, words):
        ans = []
        if len(words) == 0:
            return ans
        dic = defaultdict(list)
        self.initPrefix(words, dic)
        
        squares = []
        self.dfs(0, len(words[0]), dic, squares, ans)
        return ans
   
   
# line 37:'NoneType' object has no attribute '__getitem__'????
