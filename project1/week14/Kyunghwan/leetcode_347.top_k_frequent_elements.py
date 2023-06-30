from collections import Counter
from typing import List

nums = [1,1,1,2,2,3]
k = 2
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer =  [k for k, _ in Counter(nums).most_common(k)]
        return answer
    


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         cnt = {}
#         for num in nums:
#             if num in cnt:
#                 cnt[num]+=1
#             else:
#                 cnt[num]=1

#         target = sorted(cnt.items(), key= lambda x :-x[1])
#         answer = list(map(lambda x: x[0], target[:k]))
    
#         return answer
    





a = Solution()
print(a.topKFrequent(nums, k))