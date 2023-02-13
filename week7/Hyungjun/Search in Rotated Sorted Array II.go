func search(nums []int, target int) bool {
    l,r := 0, len(nums) - 1

    for l != r {
        mid := (l+r)/2
        if nums[mid] != target {
            if nums[l] == nums[mid] && nums[mid] == nums[r] {
                for i := l; i <= r; i ++ {
                    if nums[i] == target {
                        return true
                    }
                }
                return false
            } else {
                if nums[l] < nums[mid] && nums[mid] < nums[r] {
                    if nums[mid] > target {
                        r = mid - 1
                    } else {
                        l = mid
                    }
                } else {
                    if nums[l] <  target  && target < nums[mid] {
                        r = mid - 1
                    } else if nums[mid] < target && target <= nums[r]{
                        l = mid + 1
                    } else {
                        for i := l; i <= r; i ++ {
                            if nums[i] == target {
                                return true
                            }
                        }
                        return false
                    }
                }
            }

        } else {
            l,r = mid, mid
        }
    }
    if nums[l] == target {
        return true
    }
    return false
}
