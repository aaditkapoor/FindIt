__author__ = "Aadit Kapoor"
__version__ = "1.0.0.0"
import os
"""
    BASIC GUIDELINES
    ----------------------

    1.All helper files must end with .hl files
    2.The syntax is simple, start the question and then put a greater sign (>) followed by your answer
    3.parse_file function returns None if the search is failed
    4. Examples in the documentation
"""

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


class HelperLanguage:
    """ A class to process .hl files """
    
    status = True
    answer = ''

    def __init__(self,file_name):
        """ To intialize everything """
        self.reader = open(file_name,"r")

        if check_ext(file_name):
            self.file_name = file_name
        else:
            self.reader.close()
            rename_file(self.reader)
            
    def __str__(self):
        """ print the contents of .hl files """
        return (self.reader.read())

    def parse_file(self,question):
        """ parse the .hl file and get the answer """
            
        self.reader.seek(0,0)
        self.data = self.reader.readlines()

        if not len(self.data):
                print ("File is empty!")

        for i in range(len(self.data)):
            if question in self.data[i]:
                ans = self.data[i]
                try:
                    index = self.data[i].index('>')
                    self.answer = ans[index+1:]
                
                except:
                    self.answer = "Not found!"
                    return 'Something wrong, please check the input!'
