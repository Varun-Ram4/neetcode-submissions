class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        count = [[] for i in range(len(nums)+1)]

        for i in nums:
            group[i] = 1 + group.get(i,0) 
        for i,j in group.items():
            count[j].append(i)
        res = []
        for i in range(len(count)-1,0,-1):
            for j in count[i]:
                res.append(j)
                if len(res) == k:
                    return res