class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first, second = 0, 0
        answer = []
        while first < len(firstList) and second < len(secondList):
            if firstList[first][0] < secondList[second][0]:
                if firstList[first][1] >= secondList[second][0]:
                    if firstList[first][1] <= secondList[second][1]:
                        answer.append([secondList[second][0], firstList[first][1]])
                        first += 1
                    else:
                        answer.append([secondList[second][0], secondList[second][1]])
                        second += 1
                else:
                    first += 1
            else:
                if firstList[first][0] <= secondList[second][1]:
                    if firstList[first][1] <= secondList[second][1]:
                        answer.append([firstList[first][0], firstList[first][1]])
                        first += 1
                    else:
                        answer.append([firstList[first][0], secondList[second][1]])
                        second += 1
                else:
                    second += 1
        return answer
