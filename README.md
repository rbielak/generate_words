# generate_words

There is a science fiction book by Stanislaw Lem called [“The
Futurological Congress”](https://en.wikipedia.org/wiki/The_Futurological_Congress) in which the author describes how
futurologists in this future work. Instead of studying science,
technology and history, they use computers to generate random words
and then try to assign meanings to them.

Just for a reference think how meaningless this sentence was in 1980:
“To listen to a song, just google the title and then download the
mp3.”

Anyway, I thought that generating random words that look like words is
an interesting computer problem, so I wrote some code to try it.

My first attempt was a total failure. I generated random sequences of
letters and then tried to pick of the ones that could be words. This
resulted in mostly useless stuff.

More recently I have been reading a book called “Think Stats” and I
decided to try an apply some of statistical methods to generation of
new words. The basic idea is to analyze some existing text (more text
the better) to see the distribution of letters in a word. Then, once
the probabilities of letter occurrences are computed, words can be
generated.

My algorithm is very simple. It determines the probability of a word
of certain length occurring, and then within each given length the
probability of a particular letter happening at each position. Given
these it’s easy to generate random text.

I compute the Probability Mass Function (PMF) for distribution of word
lengths and the letter distributions (see “Thinks Stats” for gory
details). I used text of “Moby Dick” and “War and Peace” as my input
texts (you can get lots of such text from http://www.gutenberg.org/).

Also see: https://pirx2691.wordpress.com/2012/03/02/generating-random-words/
