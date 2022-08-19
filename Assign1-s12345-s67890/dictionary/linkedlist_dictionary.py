from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        # self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        # TO BE IMPLEMENTED
        self.head = None
        # Initialize next as null
        self.next = None 
        pass


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED
        listDictionary = LinkedListDictionary() #defining a dictionary linked list 


        lst = len(words_frequencies)
        
        # Sorts the Word_frequency list 
        for i in range(lst):
            for j in range(lst - i - 1):
                if (words_frequencies[j].word > words_frequencies[j + 1].word):
                        temp = words_frequencies[j].word
                        words_frequencies[j].word = words_frequencies[j + 1].word
                        words_frequencies[j + 1].word = temp
     
     #adding nodes
        for i in range(len(words_frequencies)):
            current = self.head #None
            # Adds to the head node
            if current == None:
                self.head = tuple((words_frequencies[i].word, words_frequencies[i].frequency)) 
                print(self.head)
            #If head node is full    
            else:
               #add to the next 
                # 1. Create a new node
                new_node = tuple((words_frequencies[i].word, words_frequencies[i].frequency))                
                #assignst the next node to the new data
                self.next = new_node
                print(self.next)

     
       
      
       

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found

        """


        return 0



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

        # TO BE IMPLEMENTED
        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        # TO BE IMPLEMENTED
        return []



