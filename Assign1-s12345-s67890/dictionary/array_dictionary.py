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
        
        # Sorting algorithm
        for i in range(lst):
            for j in range(lst - i - 1):
                if (words_frequencies[j].word > words_frequencies[j + 1].word):
                        temp = words_frequencies[j]
                        words_frequencies[j] = words_frequencies[j + 1]
                        words_frequencies[j + 1] = temp


        for i in range(len(words_frequencies)):
            self.array.append(tuple((words_frequencies[i].word, words_frequencies[i].frequency)))
            print(words_frequencies[i].word, words_frequencies[i].frequency)      

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
            
        low = 0
        high = len(self.array)

        while high >= low:
            mid = (high + low) // 2
            
            if self.array[mid][0] < word:
                low = mid + 1
            elif self.array[mid][0] > word:
                high = mid - 1
            else:
                return self.array[mid][1]       # returns frequency
        
            
        return 0    # not found


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        
        word = word_frequency.word
        
        low = 0
        high = len(self.array) - 1
        
        while high >= low:
            mid = (high + low) // 2            
            if self.array[mid][0] < word:
                low = mid + 1
            elif self.array[mid][0] > word:
                high = mid - 1
            else:
                
                # Returns false because this is the branch
                # executed when the word is found, thus already
                # existing in the dictionary.
                
                return False
                
        # Mid is the index that the search stops at, having
        # not found the word. In this case, that would
        # be where the word should be inserted.
        
        self.array.insert(mid, tuple((word_frequency.word, word_frequency.frequency)))

        return True
    

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        
        
        low = 0
        high = len(self.array) - 1
        
        while high >= low:
            mid = (high + low) // 2
            if self.array[mid][0] < word:
                low = mid + 1
            elif self.array[mid][0] > word:
                high = mid - 1
            else:
                                
                del self.array[mid]
                # Returns true because word to be deleted is found
                return True
        

        return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        
        ac = []
        three_most_frequent_words_from_prefix_word = []
        
        for i in self.array:
            if prefix_word in i[0][0:len(prefix_word)]:     # Checks for prefix in words
               ac.append(i)
        
        
        # Selection sort: Finds the minimum index per iteration of the inner
        # loop and then swaps it with the current index traversed in the outer loop.  
        
        if len(ac) > 0:
            for i in range(len(ac)):
                min = i
                for j in range(i + 1, len(ac)):
                    if ac[i][1] < ac[j][1]:
                        min = j
                    ac[min], ac[i] = ac[i], ac[min]

            if len(ac) <= 4:
                ac = ac[0:len(ac)]
            else:
                ac = ac[0:3]

            for i in ac:
                three_most_frequent_words_from_prefix_word.append(WordFrequency(i[0], i[1]))
        
        return three_most_frequent_words_from_prefix_word[0:3]
