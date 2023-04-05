__author__ = 'richieb'

# Zipf's law proposes how words are distributed in text. See how words are distributed
# in some classic books

import word_reader
import Cdf
import Pmf

frequency_table = {}

def load_file (fname):
    print "Loading words from file: %s " % fname
    wg = word_reader.word_getter(fname)
    for w in wg:
        key = w.lower()
        if (frequency_table.has_key(key)):
            frequency_table[key] += 1
        else:
            frequency_table[key] = 1


if __name__ == "__main__":
    load_file ("moby_dick.txt")
    load_file ("war_and_peace.txt")
    print "Word table size: %d"  % len(frequency_table)

    pmf = Pmf.MakeHistFromList(frequency_table.values())
    cdf = Cdf.MakeCdfFromPmf(pmf)

    print "Percentile 95 = %d" % (cdf.Percentile(95))
    print "Mean = %f " % (cdf.Mean())

