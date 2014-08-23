.. FindIt documentation master file, created by
   sphinx-quickstart on Mon Aug 18 06:58:15 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. toctree::
   :maxdepth: 2


FINDIT
=============
FindIt is a program that finds a given word or a letter in any file and then highlights that searched item.

It is provided with 'Words.info' for searching but you can also change it, The program comes with command line capabilties.

History.info is  a file which records your search history, this file is very important.

**FindIt comes with command line option like-:**

1. --sw (Search only a word)
2. --se (Search everything, mainly for letters. Default option)
3. --h (Some basic help)
4. --v (Version of the program)


Command Line Options
=====================
In FindIt, there are various options that can make your search better, these are only available from the command line.
FindIt consists of three command line arguments,

.. note:: If you enter any one of the command line option then you have to provide all the command line options.

* sys.argv[0] -> Program name (find.py)
* sys.argv[1] -> Word or a letter to be searched
* sys.argv[2] -> File that is to be searched
* sys.argv[3] -> Search option (--se, --sw, --li, --h)

.. warning:: Command Line options only work in the command line, except for --se option

.. topic:: Behaviour of Command Line Options
          
          * --se : Stands for **Search Everthing**
                  It searches for everything including a letter.
          * --sw : Stands for **Search a Word**
                   It searches for a specific word and show its occurences in the file, in the form (Words: <yoursearchitem> Occurences:<n number of times>)
          * --li : Stands for **license**
                   It shows the license.
          * --h : Stands for **help**
                  Displays this file

.. topic:: Some Examples

           1. $ python find.py aa Words.info --se
           2. $ python find.py aa Words.info --sw
           3. $ python find.py aa Words.info --h
           4. $ python find.py aa Words.ingo --li


Ingredients
============

FindIt contains four modules
1. FileWriter -> File writing functions which powers History.info
2. Help -> A helper language
3. Searcher -> Provides Search functions
4. Utils -> Contains utility functions

.. warning:: Only the main modules are explained below
            If you wish to learn about every module, Open that module and study the code, there are docstrings that can make you understand


FileWriter
===========

FileWriter module consists of writer.py, that writes the output in a file.
It uses json to dump the files.

.. note:: writer.py consists of a class named FileWriter

.. function:: save(self,word,fp,status,count=0)
   :module: FindIt.FileWriter

   Saves the arguments in a file using json.dump


Searcher
=========
Searcher module consists of search.py, storer,py, suggest.py. These functions provide basic searching tasks

.. note:: suggest.py consists of a class named Suggest

.. topic:: search.py
.. function:: start_searching(word,data)
   :module: FindIt.Searcher

      Search for a word or a letter in data.

.. function:: searh_word(word,data)
    :module: FindIt.Searcher

    Search for a word in data and show its occurences


   **Examples:**
    1. start_searching("aadit",["aadit","kapoor","hello","ilove google"])
    2. search_word("aadit",["aadit","kapoor","google","google"])

Help
======

    .. topic:: BASIC GUIDELINES

    1.All helper files must end with .hl files
    2.The syntax is simple, start the question and then put a greater sign (>) followed by your answer
    3.parse_file function returns None if the search is failed


    A helper file ends with .hl extension

    The format of the file must be-:

    Format::

      <Your Question> > <Your Answer>
      # Stands for comments

    The parse_file() would not accept #

    .. note::
        For more examples see, the main help file that is help.hl

    

















