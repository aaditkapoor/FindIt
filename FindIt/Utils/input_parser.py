"""
	Name: input.py
	Purpose: Provides basic parse functions
"""

import sys


def checker(arg):
    '''
         checker(str) -> bool
         Checks whether the given arg is a command or not
    '''

    if arg == 'exit':
        print ("*** EXITING ***",file=sys.stderr)
        sys.exit(0)

    elif arg == "help":
        pass

    elif arg == "history":
        show_history

    elif arg == "words":
        show_word_list()

    elif arg == "version":
        show_version


def open_docs():
    '''
        To open the documentation
    '''
    pass


def show_history():
    '''
        To open History.txt
    '''
    os.startfile('C:\\Users\Dropbox\\FindIt\\History.info')


def show_word_list():
    '''
        To show words list file
    '''
    pass


def show_version():
    '''
        To show the version of the program
    '''
    pass

