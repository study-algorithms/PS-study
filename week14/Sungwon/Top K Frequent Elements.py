import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        heap = []
        dictionary = dict()
        for i in nums:
            dictionary[i] = dictionary.get(i, 0) + 1
        
        for key, value in dictionary.items():
            heappush(heap, (-value, key))
        
        for i in range(k):
            ans.append(heappop(heap)[1])
        
        return ans
