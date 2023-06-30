class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, maxAmount = 0, len(height)-1, 0
        while right > left:
            amount = min(height[left], height[right]) * (right-left)
            maxAmount = max(amount, maxAmount)

            if height[left] >= height[right]:
                right -= 1
            else:
                left +=1
        return maxAmount
