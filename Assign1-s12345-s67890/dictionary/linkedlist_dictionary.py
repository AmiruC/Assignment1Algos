from email import header
from multiprocessing import current_process
from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        
        self.head = None

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
            
        list_of_nodes = []
        
        # Adding new nodes of the word_frequency items in an intermediate array, list_of_nodes
        for i in words_frequencies:
            new_node = ListNode(i)
            list_of_nodes.append(new_node)


        # Assigning next value of all nodes
        for i in range(len(list_of_nodes) - 1):
            list_of_nodes[i].next = list_of_nodes[i + 1]
        
        
        # Assigning head node of list
        self.head = list_of_nodes[0]


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        
        current = self.head
        while current != None:
            if current.word_frequency.word == word:
                return current.word_frequency.frequency
            current = current.next
        
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        
        new_node = ListNode(word_frequency)

        current = self.head
        while current != None:
            
            # If word exists, return false        
            if current.word_frequency.word == word_frequency.word:
                return False
            
                
            if current.next.word_frequency.word > current.word_frequency.word:
                new_node.next = current.next
                current.next = new_node
                prev = current
                return True
            current = current.next
        
        
        prev.next = new_node    # If loop is exhausted, then add new node at end of list
        
        return True
        

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        current = self.head
        while current != None:
            if current.word_frequency.word == word:
                break
            prev = current
            current = current.next
        
        
        if current == None:
            return False
        else:
            prev.next = current.next    # Remove the node
            current.next = None
            return True
        
        

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        autocompleted = []
        
        current = self.head
        while current != None:
            
            if word in current.word_frequency.word[0:len(word)]:
                autocompleted.append(current.word_frequency)
            current = current.next
        
        if len(autocompleted) > 1:

            for i in range(len(autocompleted)):
                min = i
                for j in range(i + 1, len(autocompleted)):
                    if autocompleted[i].frequency > autocompleted[j].frequency:
                        min = j
                    autocompleted[min], autocompleted[i], autocompleted[i], autocompleted[min]

        
        return autocompleted



