class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for word in strs:
            sortedWord = tuple(sorted(word))
            if sortedWord in dic.keys():
                dic[sortedWord].append(word)
            else:
                dic[sortedWord] = [word]
        ret = []

        for l in dic.values():
            ret.append(l)
        return ret