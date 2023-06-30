import string
from collections import defaultdict
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        # setting
        num2al = string.ascii_lowercase
        num_map = defaultdict()
        for i, v in enumerate(range(2,10)):
            if v not in [7,8,9]:
                num_map[v] = num2al[i*3: (i+1)*3]
            elif v == 7:
                num_map[v] = num2al[i*3: (i+1)*3+1]
            elif v == 8:
                num_map[v] = num2al[i*3+1: (i+1)*3+1]
            else:
                num_map[v] = num2al[i*3+1:]
        print(num_map)
        # combinations
        a = []
        for v in list(digits):
            a.append(num_map[int(v)])
        comb = list(itertools.product(*a))
        return [''.join(i) for i in comb]

        
