func maxSubArray(nums []int) int {
  result := nums[0]
  x := make([]int, len(nums))
  x[0] = nums[0]
  for i := 1; i < len(nums); i++ {
    if x[i-1] > 0 {
      x[i] = x[i-1] + nums[i]
    } else {
      x[i] = nums[i]
    }
    if (result < x[i]) {
      result = x[i]
    }
  }
  return result
}




// [-2,1,-3,4,-1,2,1,-5,4]
// [-2,1,-2,4,3,5,6,1,5]

// x[i] : include i, maximum subarray
// x[i] = x[i-1] + nums[i] if x[i-1] > 0 else nums[i]
