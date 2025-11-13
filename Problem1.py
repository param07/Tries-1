## Problem1 
# Implement Trie (Prefix Tree)(https://leetcode.com/problems/implement-trie-prefix-tree/)

# Method1: Using Array to store Trie Nodes with TrieNode Separate Class
# Time Complexity : O(L) -- Insert, O(L) -- Search, O(L) -- Prefix search, L = Length of the word
# Space Complexity : O(N * L) -- Insert all N words into the Trie, L = Average Length of the word
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# Search of complete word in a Trie has same time complexity as using a hashmap/hashset. It is more space efficient when
# number of words in a dictionary increases. This is because in hashset/hashmap every word is stored separately. But in trie 
# the characters can be reused. We start with a 26-sized array at the first level. At each level for a character, we 
# initialise a new Trie node corresponding to the index of the character. Each character trie node would have a separate
# array of trie nodes of 26 size. We keep a flag to mark the end of word, when a complete word gets inserted into the trie.
# When inserting a word, we iterate over the characters, and check for the existence of Trie node at the corresponding index
# of the character in the children. If it already exists, then we move our trie pointer to that character. If no trie node
# exists then we add a new trie node at the index of the character. Once the entire word gets added, we mark the flag=true
# When searching, we iterate over the word, if trie node does not exist in children for the index corresponding to the character,
# then we return false. If entire word finishes, we check the state of the flag to check if word exists or not.
# While prefix search if we are able to iterate over the entire prefix and all trie nodes exists for the characters of the prefix,
# then we return true


class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26 # array of trie nodes
        self.isEnd = False # To mark the ending of a word

class Trie(object):
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word): # TC = O(L), SC = O(N * L)
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for i in range(len(word)):
            if(not(curr.children[ord(word[i]) - ord('a')])): #checking if trie node exists for the char
                curr.children[ord(word[i]) - ord('a')] = TrieNode()

            curr = curr.children[ord(word[i]) - ord('a')]

        # word completed
        curr.isEnd = True

        

    def search(self, word): # TC = O(L)
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for i in range(len(word)):
            if(not(curr.children[ord(word[i]) - ord('a')])):
                # char does not exist in the trie
                return False

            curr = curr.children[ord(word[i]) - ord('a')]

        # word completed, check for isEnd
        return curr.isEnd
        

    def startsWith(self, prefix): # TC = O(L)
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for i in range(len(prefix)):
            if(not(curr.children[ord(prefix[i]) - ord('a')])):
                # char does not exist in the trie
                return False

            curr = curr.children[ord(prefix[i]) - ord('a')]

        # prefix finishes means it exists
        return True

print("Method1: Using Array to store Trie Nodes with TrieNode Separate Class")
words =  ["red", "cat", "rat", "rate", "cattle", "bat", "band", "andy", "ball", "cap"]
trie = Trie()
for word in words:
    trie.insert(word)

print(trie.search("cattle"))
print(trie.search("catt"))
print(trie.search("call"))
print(trie.startsWith("re"))
print(trie.startsWith("ri"))
print(trie.startsWith("and"))
print(trie.startsWith("capt"))
print(trie.search("peer"))
print(trie.startsWith("peer"))



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Method2: Using Array to store Trie Nodes with TrieNode Encapsulated Class
# Time Complexity : O(L) -- Insert, O(L) -- Search, O(L) -- Prefix search, L = Length of the word
# Space Complexity : O(N * L) -- Insert all N words into the Trie, L = Average Length of the word
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# The logic is same as above. Just we are creating Trie Node inner class instead of separate class


class Trie(object):
    # common to all objects
    class TrieNode(object):
        def __init__(self):
            self.children = [None] * 26 # array of trie nodes
            self.isEnd = False # To mark the ending of a word

    def __init__(self):
        self.root = self.TrieNode()
        

    def insert(self, word): # TC = O(L), SC = O(N * L)
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for i in range(len(word)):
            if(not(curr.children[ord(word[i]) - ord('a')])): #checking if trie node exists for the char
                curr.children[ord(word[i]) - ord('a')] = self.TrieNode()

            curr = curr.children[ord(word[i]) - ord('a')]

        # word completed
        curr.isEnd = True

        

    def search(self, word): # TC = O(L)
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for i in range(len(word)):
            if(not(curr.children[ord(word[i]) - ord('a')])):
                # char does not exist in the trie
                return False

            curr = curr.children[ord(word[i]) - ord('a')]

        # word completed, check for isEnd
        return curr.isEnd
        

    def startsWith(self, prefix): # TC = O(L)
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for i in range(len(prefix)):
            if(not(curr.children[ord(prefix[i]) - ord('a')])):
                # char does not exist in the trie
                return False

            curr = curr.children[ord(prefix[i]) - ord('a')]

        # prefix finishes means it exists
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
print("Method2: Using Array to store Trie Nodes with TrieNode Encapsulated Class")
words =  ["red", "cat", "rat", "rate", "cattle", "bat", "band", "andy", "ball", "cap"]
trie = Trie()
for word in words:
    trie.insert(word)

print(trie.search("cattle"))
print(trie.search("catt"))
print(trie.search("call"))
print(trie.startsWith("re"))
print(trie.startsWith("ri"))
print(trie.startsWith("and"))
print(trie.startsWith("capt"))
print(trie.search("peer"))
print(trie.startsWith("peer"))



# Method3: Using HashMap to store Trie Nodes with Separate TrieNode Class
# Time Complexity : O(L) -- Insert, O(L) -- Search, O(L) -- Prefix search, L = Length of the word
# Space Complexity : O(N * L) -- Insert all N words into the Trie, L = Average Length of the word
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach in three sentences only
# The logic is same as above. Just we are using hash map to store the trie nodes/children

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for i in range(len(word)):
            if(word[i] not in curr.children):
                # character does not exist
                curr.children[word[i]] = TrieNode()

            curr = curr.children[word[i]]

        # word has completed
        curr.isEnd = True           
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for i in range(len(word)):
            if(word[i] not in curr.children):
                # character does not exist
                return False
            
            curr = curr.children[word[i]]

        # check if complete word exists
        return curr.isEnd
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for i in range(len(prefix)):
            if(prefix[i] not in curr.children):
                return False

            curr = curr.children[prefix[i]]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

print("Method3: Using HashMap to store Trie Nodes with Separate TrieNode Class")
words =  ["red", "cat", "rat", "rate", "cattle", "bat", "band", "andy", "ball", "cap"]
trie = Trie()
for word in words:
    trie.insert(word)

print(trie.search("cattle"))
print(trie.search("catt"))
print(trie.search("call"))
print(trie.startsWith("re"))
print(trie.startsWith("ri"))
print(trie.startsWith("and"))
print(trie.startsWith("capt"))
print(trie.search("peer"))
print(trie.startsWith("peer"))