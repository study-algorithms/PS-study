// My implementation
func intervalIntersection(firstList [][]int, secondList [][]int) [][]int {
	p1, p2 := 0, 0
	var result [][]int
	for p1 < len(firstList) && p2 < len(secondList) {
		if firstList[p1][0] < secondList[p2][0] {
			if firstList[p1][1] < secondList[p2][0] {
				p1 += 1
			} else if firstList[p1][1] <= secondList[p2][1] {
				result = append(result, []int{secondList[p2][0], firstList[p1][1]})
				p1 += 1
			} else {
				result = append(result, []int{secondList[p2][0], secondList[p2][1]})
				p2 += 1
			}
		} else { // fistList[p1][0] >= secondList[p2][0]
			if secondList[p2][1] < firstList[p1][0] {
				p2 += 1
			} else if secondList[p2][1] <= firstList[p1][1] {
				result = append(result, []int{firstList[p1][0], secondList[p2][1]})
				p2 += 1
			} else {
				result = append(result, []int{firstList[p1][0], firstList[p1][1]})
				p1 += 1
			}
		}
	}

	return result
}


// Good Example
// public int[][] intervalIntersection(int[][] A, int[][] B) {
//     List<int[]> res = new ArrayList();
//     for (int i = 0, j = 0; i < A.length && j < B.length; ) {
//         int start = Math.max(A[i][0], B[j][0]);
//         int end = Math.min(A[i][1], B[j][1]);
//         if (start <= end)
//             res.add(new int[]{start, end});
//         if (A[i][1] < B[j][1])
//             ++i;
//         else
//             ++j;
//     }
//     return res.toArray(new int[0][]);
// }
