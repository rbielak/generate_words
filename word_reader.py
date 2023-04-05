__author__ = 'richieb'

#
# Read words from a file
#

import re

def line_getter (file_name):
    """
    Yields one line from a file on each invocation. Use like this:
    lg = line_getter ("filename.txt")
    line = lg.next()
    """
    f = open (file_name, "r")
    for line in f:
        yield line
    f.close()


def word_getter (file_name):
    """
    Yields a word from a text file. Word is define by what ever matches
    the regular expression patters "\w+". Use like this:
    wg = word_getter ("filename.txt")
    word = wg.next()
    """
    prog = re.compile ("(\w+)")
    lg = line_getter(file_name)
    for l in lg:
        # use regex to find a word
        words = prog.findall (l)
        for w in words:
            yield w



if __name__ == "__main__":
    # test of reading lines from file
    lines = line_getter("moby_dick.txt")
    for i in range(0,5):
       print (lines.next()[:-1])

    # Test getting words
    words = word_getter ("moby_dick.txt")
    for i in range (0,20):
        print (words.next())



