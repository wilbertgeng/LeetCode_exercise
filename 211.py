"""211. Design Add and Search Words Data Structure"""

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isEnd = True

    def search(self, word):
        node = self.root
        stack = [(node, word)]
        while stack:
            node, word = stack.pop()
            if not word:
                if node.isEnd:
                    return True
            elif word[0] == '.':
                for child in node.children.values():
                    stack.append((child, word[1:]))
            elif word[0] in node.children:
                node = node.children[word[0]]
                stack.append((node, word[1:]))
        return False



class WordNode:
    def __init__(self):
        self.children = collections.defaultdict(WordNode)
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]

        node.isEnd = True

    def search(self, word):
        stack = [(self.root, word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isEnd:
                    return True
            elif w[0]=='.':
                for child in node.children.values():
                    stack.append((child, w[1:]))
            else:
                if w[0] in node.children:
                    stack.append((node.children[w[0]], w[1:]))
        return False












########
