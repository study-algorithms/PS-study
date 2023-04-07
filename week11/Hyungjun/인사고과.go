import "sort"

func solution(scores [][]int) int {
	if len(scores) == 1 {
		return 1
	}
	if unable := unableCheck(scores, 0); unable {
		return -1
	}
	score := []int{scores[0][0], scores[0][1]}
	newScores := [][]int{}
	for _, v := range scores {
		if v[0]+v[1] >= score[0]+score[1] {
			newScores = append(newScores, v)
		}
	}
	scores = newScores
	newScores = [][]int{}

	sort.Slice(scores, func(i, j int) bool {
		return scores[i][0] < scores[j][0]
	})
	for i := 0; i < len(scores); i++ {
		if unable := unableCheck(scores, i); unable == false {
			newScores = append(newScores, scores[i])
		}
	}

	scores = newScores
	sort.Slice(scores, func(i, j int) bool {
		return scores[i][0]+scores[i][1] > scores[j][0]+scores[j][1]
	})

	topScore := scores[0][0] + scores[0][1]
	rank := 1
	equalPeople := 0
	for _, v := range scores {
		if topScore > v[0]+v[1] {
			topScore = v[0] + v[1]
			rank += equalPeople
			equalPeople = 1
		} else {
			equalPeople += 1
		}
		if v[0] == score[0] && v[1] == score[1] {
			return rank
		}
	}
	return rank
}

func unableCheck(scores [][]int, j int) (unable bool) { // True -> cannot get bonus
	for i := len(scores) - 1; i >= j+1; i-- {
		if scores[i][0] > scores[j][0] && scores[i][1] > scores[j][1] {
			return true
		}
	}
	return false
}
