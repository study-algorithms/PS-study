strs = ["eat","tea","tan","ate","nat","bat"]
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = dict()

        for str in strs:
            k = ''.join(sorted(str))
            if k in grouping:
                grouping[k].append(str)
            else:
                grouping[k] = [str]


        return sorted(grouping.values(), key=len)
    

a = Solution()
print(a.groupAnagrams(strs))