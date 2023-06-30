class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum = 0
        prefixSum = {0 : 1}

        for num in nums:
            sum += num
            res += prefixSum.get(sum - k, 0)
            prefixSum[sum] = prefixSum.get(sum, 0) + 1
        return res
