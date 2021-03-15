"""692. Top K Frequent Words"""

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}

        for word in words:
            d[word] = d.get(word, 0) + 1

        res = sorted(d, key = lambda word: (-d[word], word))
        #the word behind means that if their -d[word] are equal,
        #they will compare their alphabetical orders,

        return res[:k]


        
