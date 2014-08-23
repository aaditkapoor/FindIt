__author__ = "Aadit Kapoor"
__version__ = "1.0.0.0"
"""
        writer.py
        -----------

        A file to write data using json
"""


import os
import sys
import json


class FileWriter:
        """ FileWriter is used to write data into a file using json """

        def __init__(self,fp):
                """ initialize the class """

                self.name = fp
                self.fp = open(fp,mode="a")

        def save(self,word,fp,status="False",count=0):
                """ save the data into a file using json """

                json.dump("FILE THAT WAS SEARCHED: %s " % self.fp.name,self.fp)
                json.dump("Searched item: %s " % word,self.fp)
                json.dump("STATUS: %s " % status,self.fp)
                json.dump("Count: %d " % count,self.fp)

        def close(self):
                """ Close the file """
                
                self.fp.close()



