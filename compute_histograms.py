__author__ = 'richieb'
#
# Accumulate frequency of letter occurrence in words
#
import word_reader
import string

global_word_stats = {}

class Word_stats:

    def __init__(self, wl=0, count=0):
        self.word_len = wl
        self.stats = []
        self.count = 0
        i = 0
        while i < wl:
            self.stats.append ({})
            i += 1

    def add_stats (self, word):
        pos = 0;
        self.count += 1
        for letter in word.lower():
            if letter in string.ascii_letters:
                freq = self.stats[pos]
                if letter in freq:
                    freq [letter] += 1
                else:
                    freq [letter] = 1;
            pos += 1

    def print_stats (self):
        print ("*** word size = % d  Count= %d" % (self.word_len, self.count))
        for m in self.stats:
            print (m)


def update_word_stats (w):
    l = len(w)
    wstats = None
    if l in global_word_stats:
        wstats = global_word_stats[l]
    else:
        wstats = Word_stats(l)
        global_word_stats[l] = wstats
    wstats.add_stats(w)

def process_file (fname):
    print ("-- Working on file: %s " % (fname))
    wg = word_reader.word_getter(fname)
    for w in wg:
        update_word_stats (w)


if __name__ == "__main__":
    print ("Starting tests")
    process_file ("moby_dick.txt")
    process_file ("war_and_peace.txt")
    for ws in global_word_stats.values():
        ws.print_stats()
        print ("====================================")
