# fail - zero
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        # diff list
        def sign(num):
            if num > 0:
                return True
            if num < 0 :
                return False
            return 0
        diff = [sign(nums[i+1]-nums[i]) for i in range(len(nums)-1)]
        
        def possible(sub_list):
            stack = [sub_list[0]]
            for i in sub_list[1:]:
                now_ = stack[-1]
                if now_ == 0 and i != 0:
                    stack.append(i)
                elif now_ != i:
                    stack.append(i)
                else:
                    continue
            return stack

        # search for each position
        max_length = 0
        for i in range(len(diff)-1):
            temp_length = len(possible(diff[i:]))
            if temp_length > max_length:
                max_length = temp_length
            if max_length > i:
                break
        # return
        if max_length > 0:
            return max_length + 1
        return 0
