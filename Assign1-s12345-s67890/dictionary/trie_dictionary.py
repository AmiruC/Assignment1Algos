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
        lst = len(words_frequencies)
        # Orders wordfrequencies 
        for i in range(lst):
            for j in range(lst - i - 1):
                if (words_frequencies[j].word > words_frequencies[j + 1].word):
                        temp = words_frequencies[j].word
                        words_frequencies[j].word = words_frequencies[j + 1].word
                        words_frequencies[j + 1].word = temp


        cur = self.root
       
        for letter in words_frequencies:
            word = letter.word
            for c in word:
                cur.children[c] = TrieNode()
            cur.is_last = True
           



        # TO BE IMPLEMENTED


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
            else:
                
                return 2 #Needs to return the frequency 
               
            

        # TO BE IMPLEMENTED

        


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
       
        # TO BE IMPLEMENTED

        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """ 
        
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        return []
