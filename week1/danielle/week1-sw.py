def product(list):
    ans = 1
    for i in list:
        ans *= i
    return ans
def except_self(list,index):
    return list[:index] + list[index+1:]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [product(except_self(nums,i)) for i in range(len(nums))]
