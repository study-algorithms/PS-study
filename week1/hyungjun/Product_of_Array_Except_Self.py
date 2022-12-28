class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul, zero_cnt = 1, 0
        for n in nums:
            mul *= n if n!=0 else 1
            if n==0:                
                zero_cnt += 1
        mul = 0 if zero_cnt == len(nums) else mul
        ret = [mul] * len(nums)  
        for i in range(len(nums)):
            if nums[i]:
                if not zero_cnt:
                    ret[i] /= nums[i]
                    ret[i] = int(ret[i])
                else:
                    ret[i] = 0
            else: # nums[i] = 0
                ret[i] = mul if zero_cnt==1 else 0
        return ret
