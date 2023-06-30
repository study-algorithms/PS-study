height = [1,8,6,2,5,4,8,3,7]
class Solution:
    def maxArea(self, height):
        left, right = 0, len(height)-1
        maxi = (len(height)-1) * min(height[left], height[right])
        standard = min(height[left], height[right])
        while left < right:
            if height[left]< standard:
                left+=1
            elif height[right] < standard:
                right-=1
            else:
                maxi = max(maxi, (right-left)*min(height[left], height[right]))
                if height[left]>= height[right]:
                    bigger = height[left]
                    right-=1
                else:
                    bigger = height[right]
                    left+=1
        return maxi

a = Solution()
print(a.maxArea(height))