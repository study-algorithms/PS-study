class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        strs_set = []
        for s in strs:
            s_set = ''.join(sorted(s))
            if s_set not in strs_set:
                strs_set.append(s_set)
                res.append([s])
            else:
                idx = strs_set.index(s_set)
                print(idx)
                res[idx] += [s]
        return res

# cleaner
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
