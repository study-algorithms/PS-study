package project2.week3.hyungjun;


/**
 * Leetcode2405
 */
public class Leetcode2405 {
    public int partitionString(String s) {
        int result = 0;
        int flag = 0;
        for (int i = 0; i < s.length(); i++) {
            if ((flag & (1 << Integer.valueOf(s.charAt(i)-'a'))) > 0 ) {
                flag = 0;
                result += 1;
            }
            flag = flag | (1 << Integer.valueOf(s.charAt(i)-'a'));
        }
        return result;
    }
}