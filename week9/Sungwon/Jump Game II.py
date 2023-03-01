class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = [len(nums)-1] * (len(nums))
        jump[0] = 0
        
        for i in range(len(nums)-1):
            if nums[i] != 0:
                for j in range(1, nums[i]+1):
                    if i+j <= len(nums)-1:
                        jump[i+j] = min(jump[i+j], jump[i]+1)

        return jump[len(nums)-1]
