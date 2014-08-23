__author__ = "Aadit Kapoor"
__version__ = "1.0.0.0"


class Lines:
    '''
        Lines is a class which provides basic line counting function
    '''

    def __init__(self):
        pass

    count = 0
    def get_count(self):
        """ return the number of count """

        return self.count

    def get(self, file_name):
        """ get number of lines from a file(file_name) """

        with open(file_name,"rb") as f:
            for l in f:
                self.count+=1
