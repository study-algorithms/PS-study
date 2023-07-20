from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.checked = dict()
        self.s = s
        self.wordDict = wordDict

        if self.search(self.s):
            return True
        else:
            return False


    def search(self, target):
        if target in self.checked:
            return self.checked[target]
        
        if target in self.wordDict:
            return True
        
        for i in range(1, len(target)):
            if target[:i] in self.wordDict:
              # self.checked[target[:i]] = True
              if self.search(target[i:]):
                  self.checked[target] = True
                  return True
        
        self.checked[target] = False
        return False


a = Solution()
print(a.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
