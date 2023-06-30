import (
    "fmt"
)

type slicekey [3]int

func threeSum(nums []int) [][]int {
    sort.Slice(nums, func(i, j int) bool {
        return nums[i] < nums[j]
    })
    if nums[0] > 0 {
        return make([][]int, 0)
    }
    answer := make([][]int, 0)
    set := make(map[slicekey]bool)
    for i := 0; i < len(nums)-2; i++ {
        target := -nums[i]
        j := i + 1
        k := len(nums) - 1
        for j < k {
            if nums[j] + nums[k] > target {
                k--
            } else if nums[j] + nums[k] < target {
                j++
            } else {
                if _, ok := set[slicekey{nums[i], nums[j], nums[k]}]; !ok {
                    answer = append(answer, []int{nums[i], nums[j], nums[k]})
                    set[slicekey{nums[i], nums[j], nums[k]}] = true
                }
                j++
            }
        }
    }
    return answer
}
