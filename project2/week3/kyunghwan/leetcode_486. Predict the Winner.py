class Solution(object):
    def predictTheWinner(self, nums):
       self.score = 0
       self.sums = sum(nums)

       
       return self.pick(nums, True, 0) >= 0 

    def pick(self, now_nums, player1, now_score):
        if len(now_nums) == 1:
            if player1:
                return now_score + now_nums[0]
            
            return now_score -now_nums[0]

       
        if player1:
            f_choose = self.pick(now_nums[1:], False, self.sums-(now_score+now_nums[0]))
            l_choose = self.pick(now_nums[:-1], False, self.sums-(now_score+now_nums[-1]))

            return max(f_choose, l_choose)
        
        else:
            f_choose = self.pick(now_nums[1:], True, self.sums-(now_score+now_nums[0]))
            l_choose = self.pick(now_nums[:-1], True, self.sums-(now_score+now_nums[-1]))

            return min(f_choose, l_choose)


a = Solution()
print(a.pick([1,5,233,7]))
# True
