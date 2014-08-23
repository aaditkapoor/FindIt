__author__ = "Aadit Kapoor"
__version__ = "1.0.0.0"

"""
    defaults.py
    ------------
    Provides various default values in the program
"""

# Default valus to be used in the program

DEFAULT_FILE = 'Words.info'
DEFAULT_OPTION = '--se'
SELECTED_OPTION = ''

AVAILABLE_OPTIONS = ('--sw', '--h', '--v', '--li','--history','--ve')


def check_option(option):
    """
        check_option(option)
        --------------------
        Return the matched option
    """

    global SELECTED_OPTION
    global AVAILABLE_OPTIONS
    if option in AVAILABLE_OPTIONS:
        SELECTED_OPTION = option
        return SELECTED_OPTION
    else:
        return False




