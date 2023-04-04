func letterCombinations(digits string) []string {

	if len(digits) == 0 {
		return []string{}
	}
	digitToLetters := map[string]map[string]bool{
		"2": {"a": true, "b": true, "c": true},
		"3": {"d": true, "e": true, "f": true},
		"4": {"g": true, "h": true, "i": true},
		"5": {"j": true, "k": true, "l": true},
		"6": {"m": true, "n": true, "o": true},
		"7": {"p": true, "q": true, "r": true, "s": true},
		"8": {"t": true, "u": true, "v": true},
		"9": {"w": true, "x": true, "y": true, "z": true},
	}
	var result []string
	for _, d := range digits {

		if len(result) == 0 {
			for k, _ := range digitToLetters[string(d)] {
				result = append(result, k)
			}
		} else {
			var n_result []string
			for _, v := range result {
				for k, _ := range digitToLetters[string(d)] {
					n_result = append(n_result, v+k)
				}
			}
			result = n_result
		}

	}
	return result
}
