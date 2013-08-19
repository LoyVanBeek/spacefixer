#!/usr/bin/python

from collections import defaultdict

def ngrams(wordlist, n):
    """For list of words, generate sequences of n length
    >>> list(ngrams(['a', 'b', 'c', 'd'], 2))
    [('a', 'b'), ('b', 'c'), ('c', 'd')]

    >>> list(ngrams(['a', 'b', 'c', 'd'], 3))
    [('a', 'b', 'c'), ('b', 'c', 'd')]"""
    for index in range(len(wordlist[:-n])+1):
        yield tuple(wordlist[index:index+n])


def probability_map(ngrams):
    """ Calculate the probability of each n-gram occurring
    >>> ngrams =  [('a', 'b'), ('b', 'c'), ('c', 'd'), ('b', 'c')]
    >>> prob = probability_map(ngrams)
    >>> prob[('b', 'c')]
    0.5
    >>> prob[('a', 'b')]
    0.25
    >>> prob[('c', 'd')]
    0.25
    >>> prob[('z', 'z')]
    0.0
    """
    #counts = defaultdict(int)
    #Or: {ngram:ngrams.count(ngram) for ngram in set(ngrams)} #dict([(ngram, ngrams.count(ngram)) for ngram in set(ngrams)])
    # for ngram in ngrams:
    #     counts[ngram] += 1

    counts = {ngram:ngrams.count(ngram) for ngram in set(ngrams)}

    total = float(sum(counts.values()))

    probabilities = {k:(v/total) for k,v in counts.iteritems()}

    return defaultdict(float, probabilities)



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    #TRAINING:
    #   Import a corpus
    #   Build n-grams (start with n=2)
    #   Define probability for each n-gram
    #FIXING
    #   Take a sentence
    #   Shuffle the spaces around
    #       First each space separately back and forth one position, then a couple etc. 
    #   For each permutation:
    #       Get the n-grams
    #       Determine probability for n-grams. 
    #   Permutation with highest probability is the fixed sentence.

    pass