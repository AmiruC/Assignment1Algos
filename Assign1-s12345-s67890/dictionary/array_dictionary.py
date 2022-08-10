from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        
        self.array = []


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """

        lst = len(words_frequencies)
        
        for i in range(lst):

            for j in range(lst - i - 1):

                if (words_frequencies[j].word > words_frequencies[j + 1].word):
                        temp = words_frequencies[j].word
                        words_frequencies[j].word = words_frequencies[j + 1].word
                        words_frequencies[j + 1].word = temp

        # a_list = []
        for i in range(len(words_frequencies)):
            self.array.append(tuple((words_frequencies[i].word, words_frequencies[i].frequency)))
            

        print(self.array)


        return 0 
        # TO BE IMPLEMENTED


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        
        # def binary_search(Names, key):
        
        # Names should be self.array
    
        low = 0
        high = len(self.array) - 1

        while high >= low:
            mid = (high + low) // 2
            if self.array[mid] < key:
                low = mid + 1
            elif self.array[mid][0] > key:
                high = mid - 1
            else:
                return mid
            
        return -1 # not found


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
        # find the position of 'word' in the list, if exists, will be at idx-1
        
        # TO BE IMPLEMENTED
        

        return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        return []
