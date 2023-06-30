func validPalindrome(s string) bool {
    if p1, p2, ok := checkString(s); ok == true {
        return true
    } else {
        if _, _, ok := checkString(s[:p1]+s[p1+1:]); ok == true {
            return true
        }
        if _, _, ok := checkString(s[:p2]+s[p2+1:]); ok == true {
            return true
        }
    }
    return false
}

func checkString(s string) (int, int, bool) {
    p1, p2 := 0, len(s)-1
    for p1 < p2 {
        if s[p1] == s[p2] {
            p1++
            p2--
        } else {
            return p1, p2, false
        }
    }
    return p1, p2, true
}
