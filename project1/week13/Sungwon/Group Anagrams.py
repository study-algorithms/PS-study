from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for string in strs:
            dict[''.join(sorted(string))].append(string)
        
        answer = []
        for value in dict.values():
            answer.append(value)
        
        return answer
        
