mport (
    "sort"
)

type mapString struct {
    strToSlice map[string][]string
}

func runesToString(runes []rune) (outString string) {
    for _, v := range runes {
        outString += string(v)
    }
    return
}

func (ms mapString) updateStrToSlice(sortedStr, str string) {
    ms.strToSlice[sortedStr] = append(ms.strToSlice[sortedStr], str)
}

func (ms mapString) getAllValues() (allValues [][]string) {
    for k := range ms.strToSlice {
        allValues = append(allValues, ms.strToSlice[k])
    }
    return
}

func groupAnagrams(strs []string) [][]string {
    mapStrs := mapString{strToSlice: map[string][]string{}}

    for _, str := range strs {
        chars := []rune(str)
        sort.Slice(chars, func(i,j int) bool {
            return chars[i] < chars[j]
        })
        sortedStr := runesToString(chars)
        if _, ok := mapStrs.strToSlice[sortedStr]; ok {
            mapStrs.updateStrToSlice(sortedStr, str)
        } else {
            mapStrs.strToSlice[sortedStr] = []string{str}
        }
    }
    
    return mapStrs.getAllValues()
}
