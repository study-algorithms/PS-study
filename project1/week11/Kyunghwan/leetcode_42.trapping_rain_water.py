class Solution:
    def trap(self, height):
        left, right = 0, len(height)-1
        l_maxi, r_maxi = -1, -1
        tot = 0
        while left < right:
            if height[left] > height[right]:
                if height[right] > r_maxi:
                    r_maxi = height[right]
                else:
                    tot+= (r_maxi - height[right])
                right-=1
            else:
                if height[left] > l_maxi:
                    l_maxi = height[left]
                else:
                    tot+= (l_maxi - height[left])
                left+=1
        return tot


a= Solution()
print(a.trap([4,2,0,3,2,5]))