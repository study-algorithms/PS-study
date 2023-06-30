import "sort"

func solution(a []int) int {
	answer := 0
	numCnt := make([]int, len(a))
	for _, v := range a {
		numCnt[v] += 1
	}
    
    sortedCnt := [][2]int{}
    for i, v := range numCnt {
		if v > 0{
			sortedCnt = append(sortedCnt, [2]int{v,i})
		}
	}
	sort.Slice(sortedCnt, func(i, j int) bool {
		return sortedCnt[i][0] > sortedCnt[j][0]
	})
    
	for _, v := range sortedCnt {
		if v[0] > answer {
            val := 0
            for i := 0; i < len(a)-1; i++ {
                if a[i] != a[i+1] && (a[i] == v[1] || a[i+1] == v[1]) {
                    val += 1
                    i += 1
                }
            }
            if answer < val {
                answer = val
            }
        }
	}

	return answer*2
}
