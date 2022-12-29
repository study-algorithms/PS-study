class Solution:
    def productExceptSelf(self, nums):
        temp_l, temp_r = 1, 1
        answer = [1] * len(nums)
        l_idx, r_idx = 0, len(nums)-1
        
        for i in range(len(nums)):
            answer[l_idx] *= temp_l
            answer[r_idx] *= temp_r
            temp_l *= nums[l_idx]
            temp_r *= nums[r_idx]
            l_idx+=1
            r_idx-=1
        
        
        return answer

        

a= Solution()
print(a.productExceptSelf([1, 2,3, 4]))