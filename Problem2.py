## Problem2
# Longest Word in Dictionary(https://leetcode.com/problems/longest-word-in-dictionary/)

# Method1: Using set to store the dictionary
# N -- Length of the words array
# L -- Max Length of the word
# Time Complexity : O(N * (L ^ 2))
# Space Complexity : O(N*L) + O(L)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Using set to store all the entries of the words array. Going through each word in the set -- getting each substring -- checking it whether
# it exists in the set. If we get a complete word where all its substrings exist, then it is my potential longest word. I compare this word, with
# my already existing such longest word, if this current word has greater length or if it is lexicographically smaller in length if both 
# potential words are of same length, then this current word becomes my new longest word

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wordsSet = set()
        for word in words:
            wordsSet.add(word)

        ret = ""

        for word in wordsSet:
            completeWordExists = True
            for i in range(len(word)):#O(L^2)
                if(word[:i+1] not in wordsSet):#O(L)
                    completeWordExists = False
                    break
            
            if(completeWordExists):
                # the complete word exists
                if(len(word) > len(ret)):
                    ret = word
                elif(len(word) == len(ret)):
                    if(word < ret):#O(min(L,L))
                        ret = word

        return ret

words = ["w","wo","wor","worl","world", "b", "ba", "ban", "bana", "banana", "worly"]
print("Method1: Using set to store the dictionary")
sol = Solution()
print(sol.longestWord(words))


# Method2: Using trie with DFS
# N -- Length of the words array
# L -- Max Length of the word
# Time Complexity : O(N * L) -- creating trie + O(26 * N * L) = O(N * L) -- DFS
# Space Complexity : O(N*L) -- storing trie
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Storing words in a trie. Using DFS to go through all the paths. We keep going deep in a path till we keep getting true for the character in the array
# that is we have complete substrings in the words dictionary. Since we go lexicographically iterating over the children array, we only update the 
# longest result string when we get the valid string of larger length.

# Using Trie
class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie(object):
    def __init__(self):
        self.root = None

    def insert(self, word):
        if(not self.root):
            self.root = TrieNode()

        curr = self.root
        for i in range(len(word)):
            if(not curr.children[ord(word[i]) - ord('a')]):
                # character does not exist
                # create a trie node
                curr.children[ord(word[i]) - ord('a')] = TrieNode()

            curr = curr.children[ord(word[i]) - ord('a')]

        if(curr != self.root):
            curr.isEnd = True
            

class Solution(object):
    def __init__(self):
        self.longest = ""
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def helper(curr, path):
            # we would not reach the curr = null as we are checking for null here
            # if(curr.children[i] and ((curr.children[i]).isEnd)):
            # So we would not hit the base case

            if(len(path) > len(self.longest)):
                # we got a longer string
                self.longest = "".join(path)
                
            for i in range(len(curr.children)):
                if(curr.children[i] and ((curr.children[i]).isEnd)):
                    # if trie node for that character exists and it is a complete word
                    # action
                    path.append(chr(ord('a') + i))
                    # recurse
                    helper(curr.children[i], path)
                    # backtrack
                    path.pop()
                        
        # create trie with all the words
        trie = Trie()
        for word in words:# O(N * L)
            trie.insert(word)
        
        self.longest = ""
        # DFS on all the paths
        helper(trie.root, [])
        return self.longest
        
print("Method2: Using trie with DFS")
sol = Solution()
print(sol.longestWord(words))


# Method3: Using trie with BFS
# N -- Length of the words array
# L -- Max Length of the word
# Time Complexity : O(N * L) -- creating trie + O(26 * N * L) = O(N * L) -- BFS
# Space Complexity : O(26*N*L) -- storing trie + O(26*N*L) -- Queue + O(N*L) -- Path Queue
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Here for traversing the trie, we are using BFS. We go level by level and keep adding the trie nodes corresponding to the character in the queue.
# Parallely we need to maintain the current string to the current true complete word of the dictionary. This is necessary to keep track of the 
# longest word. For maintaining lexicographic order, we iterate the array at each level backwards. If we find a greater or equal string, it would 
# be the last element coming out of the queue. This happens because we are putting into the queue only those substrings that are existing in the 
# words dictionary. So trie node corresponding to the last character of the longest word would be the one left at the last in the queue.
# Iterating backwards ensures that the last word would the the lexicographically smaller word as well


# Using Trie
class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie(object):
    def __init__(self):
        self.root = None

    def insert(self, word):
        if(not self.root):
            self.root = TrieNode()

        curr = self.root
        for i in range(len(word)):
            if(not curr.children[ord(word[i]) - ord('a')]):
                curr.children[ord(word[i]) - ord('a')] = TrieNode()

            curr = curr.children[ord(word[i]) - ord('a')]

        if(curr != self.root):
            curr.isEnd = True
            
from collections import deque
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """                        
        # create trie with all the words
        trie = Trie()
        for word in words:# O(N * L)
            trie.insert(word)
        
        result = ""
        # BFS
        que = deque()
        que.append(trie.root)
        strQue = deque()
        strQue.append("")
        currStr = ""
        while(que):
            curr = que.popleft()
            currStr = strQue.popleft()
            # we can avoid this condition as the string corresponding to the last popped node would give us the longest word
            # if(len(currStr) >= len(result)):
            #     result = currStr
            for i in range(len(curr.children) - 1, -1, -1):# iterating backwards
                if(curr.children[i] and (curr.children[i].isEnd)):
                    # node exists and substring is a word in the dictionary
                    # add to the queue
                    que.append(curr.children[i])
                    # keep track of the corresponding path
                    # newStr = currStr + chr(ord('a') + i)
                    strQue.append(currStr + chr(ord('a') + i))


        return currStr
        
print("Method3: Using trie with BFS")
sol = Solution()
print(sol.longestWord(words))



# Method4: Using trie with BFS with forward iteration
# N -- Length of the words array
# L -- Max Length of the word
# Time Complexity : O(N * L) -- creating trie + O(26 * N * L) = O(N * L) -- BFS
# Space Complexity : O(26*N*L) -- storing trie + O(26*N*L) -- Queue + O(N*L) -- Path Queue
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# The Algo is same as above, just we can iterate the children array from the start front as well. So the largest would still come out as the last 
# node. If longest substrings are of equal length, then we need to keep the earlier one that is lexicographically smaller. The if condition
# helps us to keep note of both of the conditions


# Using Trie
class TrieNode(object):
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie(object):
    def __init__(self):
        self.root = None

    def insert(self, word):
        if(not self.root):
            self.root = TrieNode()

        curr = self.root
        for i in range(len(word)):
            if(not curr.children[ord(word[i]) - ord('a')]):
                # if(i < (len(word) - 1)):
                #     # the new trie node we are going to have for this character will
                #     # not further give us a valid path as it is not a word in the dictionary
                #     break
                # character does not exist
                # create a trie node
                curr.children[ord(word[i]) - ord('a')] = TrieNode()

            curr = curr.children[ord(word[i]) - ord('a')]

        if(curr != self.root):
            curr.isEnd = True
            
from collections import deque
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """                        
        # create trie with all the words
        trie = Trie()
        for word in words:# O(N * L)
            trie.insert(word)
        
        result = ""
        # BFS
        que = deque()
        que.append(trie.root)
        strQue = deque()
        strQue.append("")
        # currStr = ""
        while(que):
            curr = que.popleft()
            currStr = strQue.popleft()
            if(len(currStr) > len(result)):
                result = currStr
            for i in range(len(curr.children)):# iterating backwards
                if(curr.children[i] and (curr.children[i].isEnd)):
                    # node exists and substring is a word in the dictionary
                    # add to the queue
                    que.append(curr.children[i])
                    # keep track of the corresponding path
                    # newStr = currStr + chr(ord('a') + i)
                    strQue.append(currStr + chr(ord('a') + i))


        return result
        

print("Method4: Using trie with BFS with forward iteration")
sol = Solution()
print(sol.longestWord(words))