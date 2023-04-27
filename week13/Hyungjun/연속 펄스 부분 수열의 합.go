func solution(sequence []int) int64 {
	sequenceA := []int{}
	sequenceB := []int{}

	n := 1
	for i := 0; i < len(sequence); i++ {
		sequenceA = append(sequenceA, n*sequence[i])
		n *= -1
	}
	n = -1
	for i := 0; i < len(sequence); i++ {
		sequenceB = append(sequenceB, n*sequence[i])
		n *= -1
	}
	dpA := make([]int, len(sequence))
	dpB := make([]int, len(sequence))
	dpA[0] = sequenceA[0]
	dpB[0] = sequenceB[0]

	for i := 1; i < len(sequence); i++ {
		if dpA[i-1] > 0 {
			dpA[i] = dpA[i-1]
		}
		dpA[i] += sequenceA[i]
		if dpB[i-1] > 0 {
			dpB[i] = dpB[i-1]
		}
		dpB[i] += sequenceB[i]
	}
	result := -10 ^ 5

	for i := 0; i < len(sequence); i++ {
		if result < dpA[i] {
			result = dpA[i]
		}
		if result < dpB[i] {
			result = dpB[i]
		}
	}

	return int64(result)
}
