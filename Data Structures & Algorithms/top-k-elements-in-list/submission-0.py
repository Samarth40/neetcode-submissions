class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = []
            hashmap[i].append(i)
        sorted_hashmap = sorted(hashmap,key = lambda x : len(hashmap[x]),reverse = True)
        return list(sorted_hashmap[:k])