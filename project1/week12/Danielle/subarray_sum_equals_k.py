# # time limit
# from itertools import accumulate
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         answer = 0
#         cumsums = list(accumulate(nums))
#         cumsums = [0] + cumsums

#         for idx, cum in enumerate(cumsums):
#             for j in cumsums[idx+1:]:
#                 if j - cum == k:
#                     answer += 1
#                 if j - cum > k:
#                     continue
#         return answer

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_list = collections.Counter()
        sums_list[0] = 1
      
        sums = 0
        answer = 0
        
        for num in nums:
            sums += num
            answer += sums_list[sums-k]
            sums_list[sums] += 1

        return answer
