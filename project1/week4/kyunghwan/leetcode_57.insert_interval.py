intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x:x[0])
        

        answer = [intervals[0]]
        for start, end in intervals[1:]:
            if start > answer[-1][1]:
                answer.append([start, end])
            else:
                answer[-1][1] = max(answer[-1][1], end)
        
        return answer

a = Solution()
print(a.insert(intervals, newInterval))