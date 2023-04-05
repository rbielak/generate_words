__author__ = 'richieb'

#
# Generate words based on distribution of letters in given text
#

import Pmf
import compute_histograms


def generate_word(w_pmfs):
    word = ""
    for p in w_pmfs:
        word += p.Random()
    return word


if __name__ == "__main__":
    print ("Starting tests")
    compute_histograms.process_file("moby_dick.txt")
    compute_histograms.process_file("war_and_peace.txt")
    print ("Data collected")

    word_lengths = {}
    global_pmfs = {}
    # pick word length and create Pmfs for
    i = 0
    for i in compute_histograms.global_word_stats:
        ws = compute_histograms.global_word_stats [i]
        word_lengths[ws.word_len] = ws.count
        word_pmfs =[]
        for s in ws.stats:
            pmf = Pmf.MakePmfFromDict (s)
            word_pmfs.append (pmf)
        global_pmfs[ws.word_len] = word_pmfs

    wpmf = Pmf.MakePmfFromDict(word_lengths)

    text = ""
    for i in range (0, 100):
        rlen = wpmf.Random()
        w = generate_word(global_pmfs[rlen])
        text += w + " "

    print ("****Generated text****")
    print (text)


