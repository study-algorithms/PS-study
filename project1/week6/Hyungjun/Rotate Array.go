func rotate(nums []int, k int)  {
    k %= len(nums)
    tmp_nums := make([]int, k)
    copy(tmp_nums, nums[len(nums)-k:len(nums)])
    for _, n := range nums[:len(nums)-k] {
        tmp_nums = append(tmp_nums, n)
    }
    copy(nums, tmp_nums)
}
