func getMax(arr []int) int {
	if len(arr) == 0 {
		return 0
	}
	max := arr[0]
	for _, v := range arr {
		if v > max {
			max = v
		}
	}
	return max
}

func trap(height []int) int {
	maxH := getMax(height)
	total := maxH * len(height)
	toRemove := 0
	for _, v := range height {
		toRemove += (maxH - v)
	}
	black := total - toRemove
	black_and_blue := helper(height)
	return (black_and_blue - black)
}
func helper(height []int) (result int) {
	h1 := []int{}
	h2 := make([]int, len(height))
	tmp := 0
	for i := 0; i < len(height); i++ {
		if height[i] > tmp {
			tmp = height[i]
		}
		h1 = append(h1, tmp)
	}
	tmp = 0
	for i := len(height) - 1; i >= 0; i-- {
		if height[i] > tmp {
			tmp = height[i]
		}
		h2[i] = tmp
	}
	for i := 0; i < len(height); i++ {
		if h1[i] < h2[i] {
			result += h1[i]
		} else {
			result += h2[i]
		}
	}
	return result
}
