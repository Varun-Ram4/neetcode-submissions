class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        used = set()
        for words in range(len(strs)):
            if words in used:
                continue
            subArr = []
            for another_words in range(words,len(strs)):
                if sorted(strs[words]) == sorted(strs[another_words]):
                    subArr.append(strs[another_words])
                    used.add(another_words)
            output.append(subArr)
        return output
