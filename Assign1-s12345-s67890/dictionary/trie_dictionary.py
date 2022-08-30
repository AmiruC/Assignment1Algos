from operator import le, truediv
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
       self.root = TrieNode()
    pass

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        cur = self.root
        
        for word in words_frequencies:
            for c in word.word:
                if c not in cur.children:
                    cur.children[c] = TrieNode(letter = c)
                cur = cur.children[c]
                
            cur.frequency = word.frequency
            cur.is_last = True
            
            cur = self.root     # Reset the cur to root node



    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        cur = self.root
               
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
 
        if cur.is_last:
            return cur.frequency
        else:
            return 0
        

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
       
        cur = self.root
        
        for c in word_frequency.word:
            if c not in cur.children:
                cur.letter = c
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            
        if cur.is_last == False:    # If leaf node (word itself) doesn't exist
            cur.frequency = word_frequency.frequency
            cur.letter = c
            cur.is_last = True
            return True
        else:
            return False 


    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """ 
        
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        
        if cur.is_last == True:
            cur.is_last = False
            return True
        else:
            return False
        
        
    def traverse(self, TrieNode):
        
        ac = []
         
        for letter, trie_node in TrieNode.children.items():
            for char in self.traverse(trie_node):
                ac.append(letter + char)

        if len(TrieNode.children) == 0:
            ac.append('')
        
        return ac
            

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        autocompleted_words = []
        words = []
        cur = self.root
        
        for c in word:
            not_found = True
            for node in cur.children.values():
                if node.letter == c:
                    not_found = False
                    cur = node
                    break
            
        if not_found == False:
            words = self.traverse(cur)    #  Finds all the nodes following the prefix
            
            frequencies = []   #  Finds all the frequencies associated with the word
            for i in words:
                freq = self.search(word + i)    #  Add the prefix to the remainder of the letters found from self.traverse() for searching
                frequencies.append(freq)
                autocompleted_words.append(WordFrequency(word + i, freq))
                
        else:
            return []      #  Prefix doesn't match any words in Trie, so returns nothing


        autocompleted_words.sort(key = lambda x: x.frequency, reverse=True)

        return autocompleted_words
