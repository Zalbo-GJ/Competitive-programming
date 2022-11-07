class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word = Counter(words)
        
        h = []
        for key in word:
            heapq.heappush(h,(-word[key],key))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(h)[1])
        return ans