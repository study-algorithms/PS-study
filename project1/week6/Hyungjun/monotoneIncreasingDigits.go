import (
    "strconv"
    "strings"
)

func monotoneIncreasingDigits(n int) int {
    s := strconv.FormatInt(int64(n), 10)
    digits := strings.Split(s, "")
    l := len(digits)
    for i := l-1; i > 0; i-- {
        if digits[i] < digits[i-1]{
            l = i-1
            d, _ := strconv.Atoi(digits[i-1])
            digits[i-1] = strconv.FormatInt(int64(d-1), 10)
        }
    }
    for i := l+1; i < len(digits); i++ {
        digits[i] = "9"
    }
    
    ans,_ := strconv.Atoi(strings.Join(digits, ""))
    return ans
}
