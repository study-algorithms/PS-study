import (
    "math"
)
// first solution
func jump(nums []int) int {
    d := make([]int, len(nums))
    d[0] = 0
    for i := 1; i < len(nums); i++ {
        d[i] = math.MaxInt32
    }
    for i := 1; i < len(nums); i++ {
        for j := 0; j < i; j++ {
            if nums[j] + j >= i {
                if d[j] + 1 < d[i] {
                    d[i] = d[j] + 1
                }
            }
        }
    }
    return d[len(nums)-1]
}

// second solution
func jump(nums []int) int {
    p1, p2 := 0,0 // p1 is currentyl reachable position, p2 is next maximum position
    count := 0
    for i := 0; i < len(nums) - 1; i++ {
        if p2 < i + nums[i] {
            p2 = i + nums[i]
        }
        if p1 == i {
            p1 = p2
            count++
        }
        if p1 >= len(nums) - 1 {
            return count
        }
    }
    return count
}
