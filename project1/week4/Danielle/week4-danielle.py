class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # sort by starts
        res = intervals + [newInterval]
        res.sort(key = lambda x : x[0])
        # non overlap filtering
        def nonoverlap(List):
            """chech if the lists in the list are non-overlapping"""
            if len(List)<=1:
                return List
            res = []
            temp = []
            for i in range(len(List)-1):
                if len(temp)==0:
                    temp = List[i]
                current_end = temp[1]
                next_start = List[i+1][0]
                if next_start - current_end >= 1:
                    res.append(temp)
                    temp = []
                    if i+1 == len(List)-1:
                        print(List[i+1])
                        res.append(List[i+1])
                else:
                    temp += List[i+1]
                    temp = [min(temp), max(temp)]
                    if i+1 == len(List)-1:
                        res.append(temp)
            return res
        return nonoverlap(res)
