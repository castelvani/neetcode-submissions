class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        hash = {}
        groupKey = 0

        for i, word in enumerate(strs):
            sortedWord = "".join(sorted(word))

            if sortedWord not in hash:
                hash[sortedWord] = groupKey
                groupKey+=1
                groups.append([word])
            else:
                groups[hash[sortedWord]].extend([word])

        return groups
