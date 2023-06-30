func singleNonDuplicate(nums []int) int {
    l, r := 0, len(nums)-1
    if l == r {
        return nums[l]
    }
    for l < r {
        m := (l+r)/2
        if nums[m] != nums[m-1] && nums[m] != nums[m+1] {
            return nums[m]
        }
        if (m - l) % 2 == 1 {
            if nums[m] == nums[m-1] {
                l = m + 1
            } else { // nums[m] == nums[m+1]
                r = m - 1
            }
        } else {
            if nums[m] == nums[m-1] {
                r = m
            } else { // nums[m] == nums[m+1]
                l = m
            }
        }
    }
    return nums[l]
}
