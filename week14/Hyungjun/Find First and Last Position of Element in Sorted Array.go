func searchRange(nums []int, target int) []int {
	start := findFirstOccurrence(nums, target)
	if start == -1 {
		return []int{-1, -1}
	}

	end := findLastOccurrence(nums, target)
	return []int{start, end}
}

func findFirstOccurrence(nums []int, target int) int {
	low, high := 0, len(nums)-1
	result := -1

	for low <= high {
		mid := low + (high-low)/2
		if nums[mid] == target {
			result = mid
			high = mid - 1
		} else if nums[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return result
}

func findLastOccurrence(nums []int, target int) int {
	low, high := 0, len(nums)-1
	result := -1

	for low <= high {
		mid := low + (high-low)/2
		if nums[mid] == target {
			result = mid
			low = mid + 1
		} else if nums[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return result
}
