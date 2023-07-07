#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer = {-1, -1};
    unordered_set<string> us, us2;
    for (auto& gem: gems) us.insert(gem);
    int jewels = us.size();
    
    int windowsStart = 0, windowsEnd = 0;
    for (int i = 0; i < gems.size(); i++) {
        us2.insert(gems[i]);
        if (us2.size() == jewels) break;
        
        while ((gems[windowsStart] == gems[windowsStart+1] || gems[windowsStart] == gems[windowsEnd]) && windowsStart != windowsEnd) {
            windowsStart++;
        }
        windowsEnd++;
        answer[0] = windowsStart+1;
        answer[1] = windowsEnd+1;
    }
    if (answer[0] == -1 || answer[1] == -1) return {1, 1};
    
    return answer;
}
