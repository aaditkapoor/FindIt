__author__ = "Aadit Kapoor"
__version__ = "1.0.0.0"

import os

# Required Extension
REQ_EXT = 'hl'

def check_ext(file_name):
    """ check the extension of the given file """

    # Checking the file
    if file_name[-2:] == 'hl':
        return True
    else:
        return False

def rename_file(file):
    """ rename the file to .hl """

    if file.closed:
        try:
            os.rename(file.name,file.name[0:len(file.name) - 2])
        except:
            print ("Something wrong!!")
