"""127. Word Ladder"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]]) #double pairs brackets

        charset = set() # create a set to store letters
        for word in wordList:
            for w in word:
                charset.add(str(w)) # add strings!

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length

            for i in range(len(word)):
                for l in charset:
                    next_word = word[:i] + l + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1]) # single pair brackets

        return 0
