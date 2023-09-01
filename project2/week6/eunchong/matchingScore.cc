#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <regex>

using namespace std;

string toLower(const string str) {
    string lowerCaseStr = str;
    transform(lowerCaseStr.begin(), lowerCaseStr.end(), lowerCaseStr.begin(),
        [](unsigned char c){ return tolower(c); });

    return lowerCaseStr;
}

int countMatch(const string text, const string target_str) {
    string data = toLower(text);
    string target = toLower(target_str);

    regex word_regex("\\b" + target + "\\b");

    auto words_begin = sregex_iterator(data.begin(), data.end(), word_regex);
    auto words_end = sregex_iterator();

    return distance(words_begin, words_end);
}

void countRef(const string page) {

}

int solution(string word, vector<string> pages) {

}
