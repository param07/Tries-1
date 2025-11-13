## Problem3
# Replace Words (https://leetcode.com/problems/replace-words/)

# Method1: Using Trie with search
# N = No. of words in the dictionary
# L = Average length of the word
# M = No. of words in the sentence
# Time Complexity : O(N*L) -- Insert + O(M * L) --- Search
# Space Complexity : O(N * L) -- Insert all N words into the Trie + O(M * L) -- creating the final replacement sentence
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# We insert the dictionary of words in the trie. Where a word ends we store the actual word in the trie for that last character.
# Here we can do an optimization while inserting words. If we find a word, whose smaller prefix we already have in the trie, then we
# dont need to insert the longer word as we require the smallest root words for replacement.
# Then we split the sentence into words. Then we iterate over the sentence array, for each word we search character by character in
# the trie. If we dont find the replacement word, then we reuse the actual word.

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.wordEnd = None # to keep track of dictionary words when completed

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word): # TC = O(L)
        curr = self.root

        for i in range(len(word)):
            if(word[i] not in curr.children):
                curr.children[word[i]] = TrieNode()
            
            # Optimization -- no need to add words of larger length if smaller already exists
            # with similar prefix before the bigger one
            if(curr.wordEnd):
                return
            curr = curr.children[word[i]]

        curr.wordEnd = word

    def search(self, word): # TC = O(L)
        # implement a modified search
        # return word where you find the first wprd
        curr = self.root

        for i in range(len(word)):
            if(word[i] not in curr.children):
                return None

            curr = curr.children[word[i]]
            if(curr.wordEnd):
                return curr.wordEnd
        
        return None

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # build trie for dictionary
        trie = Trie()
        for word in dictionary: # TC = O(N * L) = O(10^6)
            trie.insert(word)

        sentenceArr = sentence.split()
        result = []
        for i in range(len(sentenceArr)): #TC = O(10^6)
            trieWord = trie.search(sentenceArr[i])
            if(trieWord):
                result.append(trieWord)
            else:
                result.append(sentenceArr[i])

        return " ".join(result)


sol = Solution()
print("Method1: Using Trie with search")
print(sol.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(sol.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))


# Method2: Using Trie without storing words
# N = No. of words in the dictionary
# L = Average length of the word
# M = No. of words in the sentence
# Time Complexity : O(N*L) -- Insert + O(M * L) --- Search
# Space Complexity : O(N * L) -- Insert all N words into the Trie + O(M * L) -- creating the final replacement sentence
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# The logic is same as above. Here we are not storing the words in the trie. While searching the word/prefix in the trie
# we are keeping track of the matching characters of the sentence word and word in the trie. We return the word if we find in the 
# trie.

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False # to keep track of dictionary words when completed

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word): # TC = O(L)
        curr = self.root

        for i in range(len(word)):
            if(word[i] not in curr.children):
                curr.children[word[i]] = TrieNode()
            
            # Optimization -- no need to add words of larger length if smaller already exists
            # with similar prefix before the bigger one
            if(curr.isEnd):
                return
            curr = curr.children[word[i]]

        curr.isEnd = True

    def search(self, word): # TC = O(L)
        # implement a modified search
        # return word where you find the first wprd
        curr = self.root
        replacement = []

        for i in range(len(word)):
            if(word[i] not in curr.children):
                return ""

            curr = curr.children[word[i]]
            replacement.append(word[i])
            if(curr.isEnd):
                return "".join(replacement)
        
        return ""

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # build trie for dictionary
        trie = Trie()
        for word in dictionary: # TC = O(N * L)
            trie.insert(word)

        sentenceArr = sentence.split()
        result = []
        for i in range(len(sentenceArr)):
            trieWord = trie.search(sentenceArr[i])
            if(trieWord):
                result.append(trieWord)
            else:
                result.append(sentenceArr[i])

        return " ".join(result)
    

sol = Solution()
print("Method2: Using Trie without storing words")
print(sol.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(sol.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))


# Method3: Using Trie without search function
# N = No. of words in the dictionary
# L = Average length of the word
# M = No. of words in the sentence
# Time Complexity : O(N*L) -- Insert + O(M * L) --- Search
# Space Complexity : O(N * L) -- Insert all N words into the Trie + O(M * L) -- creating the final replacement sentence
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# The logic is same as above. Here we are implementing the search in the trie inside the main function itself and not 
# creating a separate search in the trie class

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False # to keep track of dictionary words when completed

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word): # TC = O(L)
        curr = self.root

        for i in range(len(word)):
            if(word[i] not in curr.children):
                curr.children[word[i]] = TrieNode()
            
            # Optimization -- no need to add words of larger length if smaller already exists
            # with similar prefix before the bigger one
            if(curr.isEnd):
                return
            curr = curr.children[word[i]]

        curr.isEnd = True


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # build trie for dictionary
        trie = Trie()
        for word in dictionary: # TC = O(N * L)
            trie.insert(word)

        sentenceArr = sentence.split()
        result = []
        for i in range(len(sentenceArr)):
            if(i > 0):
                # adding space to the front of the word. Dont add space in front of the first word. Rest all you can add
                result.append(" ")
            currWord = sentenceArr[i]
            curr = trie.root
            replacement = []
            for j in range(len(currWord)):
                # if trie node for current character does not exist or we
                # found a prefix in trie
                if((currWord[j] not in curr.children)):
                    break

                curr = curr.children[currWord[j]]
                replacement.append(currWord[j])
                if(curr.isEnd):
                    break

            if(curr.isEnd):
                # if we found the word
                result.append("".join(replacement))
            else:
                # did not find the word
                result.append(currWord)
                


        return "".join(result)

sol = Solution()
print("Method3: Using Trie without search function")
print(sol.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(sol.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))


# Method4: Using Hashset
# N = No. of words in the dictionary
# L = Average length of the word
# M = No. of words in the sentence
# Time Complexity : O(N*L) -- Insert + O(M * (L^2)) --- Search
# Space Complexity : O(N * L) -- Insert all N words into the Hashset + O(M * L) -- creating the final replacement sentence
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Here we first put all the dictionary words in a hashset. Then we split our sentence into array of words. For each word, for its
# every possible prefix, we try to find the min length prefix that exists in the hashset. So this searching for all possible 
# prefix for a sentence word in hashset takes O(L^2) time complexity. So searching all sentence word takes O(M * (L^2)) time 
# complexity. When we find a prefix, we replace the word with the prefix. If we dont find the prefix, we reuse the same sentence
# word

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        # Using hashset
        wordsSet = set()
        # TC = O(N * L)
        for word in dictionary:
            wordsSet.add(word)

        sentenceArr = sentence.split()
        # SC = O(M * L)
        result = []
        for i in range(len(sentenceArr)): # TC = O(M * (L^2))
            if(i > 0):
                result.append(" ")
            result.append(sentenceArr[i])
            for j in range(len(sentenceArr[i])): # TC = O(L^2)
                prefix = sentenceArr[i][:j+1] # TC = O(L)
                if(prefix in wordsSet): # TC = O(L)
                    result[-1] = prefix
                    break

        return "".join(result)

sol = Solution()
print("Method4: Using Hashset")
print(sol.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))
print(sol.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))