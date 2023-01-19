class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = [False] * len(nums)
        stack = [0]

        while stack:
            value = stack.pop()
            if value == len(nums)-1:
                return True
            visited[value] = True
            for jump in range(1, nums[value]+1):
                if value+jump < len(nums) and not visited[value+jump]:
                    stack.append(value+jump)
        
        return False
