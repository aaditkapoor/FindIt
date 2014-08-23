__author__ = "Aadit Kapoor"
__version__ = "1.0.0.0"

"""
     Name: error.py
     Purpose: Provides basic errot reporting functins
"""

import sys


def raise_find_error(word):
    """
         raise_find_error(str) -> str
         print error message in an interactive way
         Occurs when word is not found
    """

    print ("*** WORD NOT FOUND ***: %s" % word, file=sys.stderr)


def file_error():
    """
         file_error() -> str
         Occurs when there is an error in opening the file
    """

    print  ("*** ERROR ***: Error in opening file", file = sys.stderr)
