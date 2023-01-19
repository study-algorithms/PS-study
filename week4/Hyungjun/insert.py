class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        k = 0
        for i in range(len(intervals)):
            si, ei = intervals[i]

            if not k and newInterval[k] >= si and newInterval[k] <= ei:
                k += 1
                j = i
                while j < len(intervals):
                    if newInterval[k] >= intervals[j][0]:
                        intervals[i][1] = max(intervals[j][1], newInterval[k])
                    else:
                        return intervals[:i+1] + intervals[j:]
                    j += 1
                return intervals[:i+1] + intervals[j:]
            if not k and newInterval[k] < si:
                if newInterval[k+1] < si:
                    return intervals[:i] + [newInterval] + intervals[i:]
                intervals[i][0] = newInterval[k]
                k += 1
                j = i
                while j < len(intervals):
                    if newInterval[k] >= intervals[j][0]:
                        intervals[i][1] = max(intervals[j][1], newInterval[k])
                    else:
                        return intervals[:i+1] + intervals[j:]
                    j += 1
                return intervals[:i+1] + intervals[j:]
        
        return intervals + [newInterval]
