func maxArea(height []int) int {
    p1, p2 := 0, len(height) - 1 
    answer := 0

    for p1 < p2 {
        minh := 0
        if height[p1] < height[p2] {
            minh = height[p1]
        } else {
            minh = height[p2]
        }
        if answer < minh * (p2-p1) {
            answer = minh * (p2-p1)
        }
        for p1 < p2 && height[p1] <= minh {
            p1 += 1
        }
        for p1 < p2 && height[p2] <= minh {
            p2 -= 1
        }
    }
    return answer
}
