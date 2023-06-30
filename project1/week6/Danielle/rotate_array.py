class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # simple try
        k %= len(nums) # added
        nums[:] = nums[-k:]+nums[:-k] # [:] added

    # #  O(1) space
    # def rotate(self, nums: List[int], k: int) -> None:
    #     def reverse(start, end): # helper method to reverse from start to end
    #         while start < end: # while there is stuff to reverse
    #             nums[start], nums[end] = nums[end], nums[start] # swap the elements at the ends
    #             start, end = start + 1, end - 1 # move pointers closer to each other
                
    #     n = len(nums)
    #     k %= n
    #     reverse(0,n-1) # reverse full list
    #     reverse(0,k-1) # reverse first k elements (previously the last k elements)
    #     reverse(k,n-1) # reverse the rest of the list
