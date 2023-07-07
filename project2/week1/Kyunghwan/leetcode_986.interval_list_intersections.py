from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            
            left, right = max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])
            
            # 겹치는지 여부
            if left <= right:
                answer.append([left, right])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return answer
    
a = Solution()
print(a.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))