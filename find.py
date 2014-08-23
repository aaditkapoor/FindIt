#usr/bin/python
__author__ = "Aadit Kapoor"
__version__ = "1.0.0"

"""
    FINDIT
    =============

    FindIt is a program that finds a given word or a letter in any file and then highlights that searched item.

    It is provided with 'Words.info' for searching but you can also change it, The program comes with command line capabilities.

    History.info is  a file which records your search history, this file is very important.

    FindIt comes with command line option like-:
    1. --sw (Search only a word)
    2. --se (Search everything, mainly for letters. Default option)
    3. --h (Open Documentation)
    4. --v (Version of the program)
"""

# important imports
from FindIt.Searcher import search, storer, suggest
from FindIt.FileWriter import writer
from FindIt.Utils import lines, error, input_parser, display, defaults
from FindIt.Help import helper
# Setting the class
class MainProgram(lines.Lines):
    """
        MainProgram is a class which handles all the program
        Its memebers include

        1.data (list)
        2.words_file (file)
        6.OPTION (str)
        7.word (str)
        8.file_name (file)

    """

    data = []
    words_file = None
    #file_history = None

    # try-except for command line version
    try:
        OPTION = defaults.check_option(sys.argv[3])  # Getting the required option
        if not OPTION:
            print ('Invalid option')
            print ('Taking DEFAULT.OPTION!')
            OPTION = defaults.DEFAULT.OPTION
    except:
        OPTION = defaults.DEFAULT_OPTION

    # try-except for command line version
    try:
        word = sys.argv[1]
        file_name = sys.argv[2]
    except:
        word = ''
        file_name = defaults.DEFAULT_FILE
    # -----------------------------------------------

    def __init__(self):
        """
            __init__
            -----------
            A constructor to initialize the word and the file_name
        """
        self.count = 0
        try:
            self.words_file = open(self.file_name, "r")
            self.file_history = open("History.info", "a")
        except IOError:
            error.file_error()
            print ('Exiting')
            sys.exit()
        finally:
            # Greeting message
            print ('====== ==== FINDIT ====== ====')
            print ('BUILD 1000 [VERSION: 1.0.0.0]')
            print ('STATUS: Opening operation done!')
            print

    def start(self):
        """
            start()
            --------
            Provides the basic modification statements for the file
        """

        self.data = storer.store_data(self.words_file)
        self.lines = lines.Lines.get(self, self.file_name)
        storer.remove_slashn(self.data)
        storer.to_lower(self.data)

    def close(self):
        """
            close()
            -------
            Closes the file
        """

        self.words_file.close()

    def get_input(self):
        """
            get_input() to get data from user and show a beautiful message of init
        """

        print ('Total number of lines: %d' % lines.Lines.get_count(self))

        if not self.word: # Checking for command line input
            self.word = input("Enter an item to be searched (Type \'exit\' to exit) :  ")
            input_parser.checker(self.word)

    def start_search(self):
        """
            Main function of the program to search for a whole word or just a letter and highlight it.
            It also keeps the record of your entered data in History.txt
        """
        file_writer = writer.FileWriter("History.info")

        if self.OPTION == '--se':
            c = search.start_searching(self.word, self.data)
            print (sep='\n')
            if c >= 1:
                print ("Word found: %s\n" % self.word)
                display.show("PASS!!")
                file_writer.save(word=self.word, fp = self.words_file, status = True, count = c)

            else:
                s = suggest.Suggest(self.word, self.data)
                print ("Word not found: %s\n" % self.word)
                display.show("FAILED")
                file_writer.save(word=self.word, fp = self.words_file, status = False, count = c)



        elif self.OPTION == '--sw':
            search.search_word(self.word, self.data)

        elif self.OPTION == '--h':
            print ('Opening doc....')
            time.sleep(2)
            try:
                os.startfile('C:\\Users\\Aadit\\Dropbox\\FindIt\\docs\\_build\\html\\index.html')
            except:
                print ('Error in opening doc file!!')
    
        elif self.OPTION == '--v':
            input_parser.show_version()
        elif self.OPTION == '--li':
            license()

        elif self.OPTION == '--history':
            input_parser.show_history()


def main():
    """
        Entry function of the whole program
    """
    # Instance of the class
    Main = MainProgram()


    # Start
    Main.start()

    # Ready
    Main.close()

    # Get data
    Main.get_input()

    # Start the search (or GO!!!)
    Main.start_search()

    if Main.OPTION == '--se' or Main.OPTION == '--sw':
        print ('Press any key to save!')
        a = input()


# Exploding

if __name__ == "__main__":
    main()

