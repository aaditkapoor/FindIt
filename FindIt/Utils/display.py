__author__ = "Aadit Kapoor"
__version__ = "1.0.0"

"""
    Name: display.py
    Purpose: Provides basic displaying functions
"""

import time
import sys

def show(msg):
    '''
        show(msg) -> str
        Print a message in an interative way
    '''
    print ("*** STATUS: %s ***" % msg, file=sys.stderr)
