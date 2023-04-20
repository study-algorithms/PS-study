func subarraySum(nums []int, k int) int {
	answer := 0
	s := make([]int, len(nums))
	t := 0
	for i, v := range nums {
		t += v
		s[i] = t
		if s[i] == k {
			answer += 1
		}
	}
	for i := 1; i < len(nums); i++ {
		for j := i; j < len(nums); j++ {
			if s[j]-s[i-1] == k {
				answer += 1
			}
		}
	}
	return answer
}
