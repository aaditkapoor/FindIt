__author__ = "Aadit Kapoor"
__version__ = "1.0.0.0"

import random
import sys

"""
	Suggest module to suggest words when search is failed
"""


class Suggest:
    def __init__(self, word, data):
        self.data = data
        self.word = word

    def suggest_word(self):
        l = len(self.word)

        index_number = random.randint(0, l - 1)

        for i in range(len(self.data)):

            index = self.data[i].find(self.word[index_number])

            if index == -1:
                return 'Not found!'
            else:
                return self.data[index]






